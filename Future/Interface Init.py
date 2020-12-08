from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Container Simulation")

mainframe = ttk.Frame(root, padding="9 9 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
#
feet = StringVar()
meters = StringVar()
cntr = StringVar()
phone = StringVar()

cntr20 = StringVar(mainframe, value='28')
cntr40 = StringVar(mainframe, value='58')
cntr40HC = StringVar(mainframe, value='68')
cntr45 = StringVar(mainframe, value='78')
#
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))


photo = PhotoImage(file = "logo.png")
logo = Label(image=photo)
logo.grid(column=0, row=0, sticky=(N, W))
logo.image = photo # keep a reference!


#1:
#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#space filler:
ttk.Label(mainframe, text="  ").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="  ").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="  ").grid(column=0, row=3, sticky=W)




#Title sorta
ttk.Label(mainframe, text="Container Simulator", font='Times 16').grid(column=0, row=4, sticky=W)

#2
ttk.Label(mainframe, text="20' Container").grid(column=0, row=5, sticky=W)
Cntr20Max = ttk.Entry(mainframe, width=7, textvariable=cntr20).grid(column=1, row=5, sticky=(W, E))
Cntr20Yes = ttk.Radiobutton(mainframe, text='Enable', variable=phone, value='xCntr20Yes').grid(column=3, row=5, sticky=W)
Cntr20No = ttk.Radiobutton(mainframe, text='Disable', variable=phone, value='xCntr20No').grid(column=4, row=5, sticky=W)



#40
ttk.Label(mainframe, text="40' Container").grid(column=0, row=6, sticky=W)
Cntr40Max = ttk.Entry(mainframe, width=7, textvariable=cntr40).grid(column=1, row=6, sticky=(W, E))
Cntr40Yes = ttk.Radiobutton(mainframe, text='Enable', variable=phone, value='xCntr40Yes').grid(column=3, row=6, sticky=W)
Cntr40No = ttk.Radiobutton(mainframe, text='Disable', variable=phone, value='xCntr40No').grid(column=4, row=6, sticky=W)

#40HC
ttk.Label(mainframe, text="40HC Container").grid(column=0, row=7, sticky=W)
Cntr40HCMax = ttk.Entry(mainframe, width=7, textvariable=cntr40HC).grid(column=1, row=7, sticky=(W, E))
Cntr40HCYes = ttk.Radiobutton(mainframe, text='Enable', variable=phone, value='xCntr40HCYes').grid(column=3, row=7, sticky=W)
Cntr40HCNo = ttk.Radiobutton(mainframe, text='Disable', variable=phone, value='xCntr40HCNo').grid(column=4, row=7, sticky=W)

#45
ttk.Label(mainframe, text="45' Container").grid(column=0, row=8, sticky=W)
Cntr45Max = ttk.Entry(mainframe, width=7, textvariable=cntr45).grid(column=1, row=8, sticky=(W, E))
Cntr45Yes = ttk.Radiobutton(mainframe, text='Enable', variable=phone, value='xCntr45Yes').grid(column=3, row=8, sticky=W)
Cntr45No = ttk.Radiobutton(mainframe, text='Disable', variable=phone, value='xCntr45No').grid(column=4, row=8, sticky=W)

#DONE~!!!
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=9, sticky=(W, E))
ttk.Button(mainframe, text="Done", command=calculate).grid(column=3, row=9, sticky=W)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
