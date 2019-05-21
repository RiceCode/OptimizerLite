
class Init:
    def __init__(self):
        self.useLcl = True
        self.use20 = True
        self.use40 = True
        self.use40HC = True
        self.use45 = True

        self.sizeLcl = 1
        self.size20 = 27
        self.size40 = 57
        self.size40HC = 67
        self.size45 = 76
        self.minLoad20 = 20



    def Prompt(self):
        while True:
            decision = input("Hi, would you like to use all the default values? Type Yes, No, or Help.").lower()
            if decision == "yes":
                break
            if decision == "help":
                    print("Default means the following will be allowed:")
                    print("LCL = %d"  %self.sizeLcl)
                    print("20' = %d"  %self.size20)
                    print("40' = %d"  %self.size40)
                    print("40HC = %d"  %self.size40HC)
                    print("45' = %d"  %self.size45)
            if decision == "no":
                    change = input("Would you like to change Container CBM or Container Type Allowed?").lower()
                    if(change.lower() == "container cbm"):
                        self.minLoad20 = int(input("What's the minimum loadability for 20'? Anything lower will be in LCL"))
                        self.size20 = int(input("What is the maximum CBM you would like for your 20'"))
                        self.size40 = int(input("What is the maximum CBM you would like for your 40'"))
                        self.size40HC = int(input("What is the maximum CBM you would like for your 40HC"))
                        self.size45 = int(input("What is the maximum CBM you would like for your 45'"))
                        print("The default values has been updated.")
                    if(change.lower() == "container type allowed"):
                        self.useLcl = int(input("Should 20' be used? Please reply True or False)"))
                        print("use20 = " + self.useLcl)
                        self.use20 = int(input("Should 20' be used? Please reply True or False)"))
                        print("use20 = " + self.use20)
                        self.use40 = int(input("Should 40' be used? Please reply True or False)"))
                        print("use40 = " + self.use40)
                        self.use40HC = int(input("Should 40HC be used? Please reply True or False)"))
                        print("use40HC = " + self.use40HC)
                        self.use45 = int(input("Should 45' be used? Please reply True or False)"))
                        print("use45 = " + self.use45)
                        print("The default values has been updated.")


        #Container being used:
        self.sizeLcl = self.CheckNotUsed(self.useLcl, self.sizeLcl)
        self.size20 = self.CheckNotUsed(self.use20, self.size20)
        self.size40 = self.CheckNotUsed(self.use40, self.size40)
        self.size40HC = self.CheckNotUsed(self.use40HC, self.size40HC)
        self.size45 = self.CheckNotUsed(self.use45, self.size45)

        return(self.sizeLcl, self.minLoad20, self.size20, self.size40, self.size40HC, self.size45)


    def CheckNotUsed(self, containerType, containerSize):
        if containerType == False:
            #print("Im returning 0")
            return 0
        else:
            #print("Im returning containerSize")
            return containerSize




