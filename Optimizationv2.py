from pulp import *

class Optimization:
    def __init__(self, x20, x40, x40HC, x45, passedIn):
        #costs:
        self.cntr20Cost = 2500
        self.cntr40Cost = 3000
        self.cntr40HCCost = 3200
        self.cntr45Cost = 3500

        self.cntr20Max = x20
        self.cntr40Max = x40
        self.cntr40HCMax = x40HC
        self.cntr45Max = x45

        self.CBM = passedIn


    def LP(self):
        #direction:
        prob = pulp.LpProblem("Container Optimization", LpMinimize)


        #Decision Variables
        x1 = pulp.LpVariable("20'", 0, None, LpInteger)
        x2 = pulp.LpVariable("40'", 0, None, LpInteger)
        x3 = pulp.LpVariable("40HC", 0, None, LpInteger)
        x4 = pulp.LpVariable("45", 0, None, LpInteger)


        #Objective Function
        prob += self.cntr20Cost * x1 + self.cntr40Cost * x2 + self.cntr40HCCost * x3 + self.cntr45Cost * x4, "Total Cost"

        #Constraints
        prob += self.cntr20Max*x1 + self.cntr40Max*x2 + self.cntr40HCMax*x3 + self.cntr45Max*x4 >= self.CBM   #Must take all cargos

        prob.solve()

        #determine utilization:
        util = utilizationCalc(self, self.CBM, x1.varValue, x2.varValue, x3.varValue, x4.varValue)


        #For printing purposes:
        # print("Status: ", LpStatus[prob.status])
        # for v in prob.variables():
        #     print(v.name, "=", v.varValue)

        return x1.varValue, x2.varValue, x3.varValue, x4.varValue, util


##
# Param: cntr20Cnt = number of cntr20 used.
#        cntr40Cnt = number of cntr40 used
#        cntr40HC = number of cntr40HC used.
#        cntr45Cnt = number of cntr45cnt used.
##
def utilizationCalc(self, CBM, cntr20Cnt, cntr40Cnt, cntr40HCCnt, cntr45Cnt):
    y1 = int(cntr20Cnt)
    y2 = int(cntr40Cnt)
    y3 = int(cntr40HCCnt)
    y4 = int(cntr45Cnt)

    currentCntrMax = self.cntr20Max*y1 + self.cntr40Max*y2 + self.cntr40HCMax*y3 + self.cntr45Max*y4      #maximum CBM based on number of container selected.

    try:
        utilPercent = round(CBM/(currentCntrMax)*100, 1)
        utilPercent = str(utilPercent) + "%"
        #print(utilPercent)
        return utilPercent
    except:
        utilPercent = "error"
        return utilPercent







