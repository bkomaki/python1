# -*- coding: cp1256 -*-
import os
try:
    import Tkinter as tk
    import  tkFileDialog as filedialog
    import ttk
except:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import ttk

#################   
root = tk.Tk()
root.title(u'محاسبه شاخص خشکسالي')
nb=ttk.Notebook(root)
page1=ttk.Frame(nb )
page1.grid_propagate(False)
nb.add(page1,text="SPI")
nb.pack(expand=1, fill="both")    
####input##############
    
label0= tk.Label(nb, text=u"فايل ورودي"  ,
                fg="white",bg="blue",
                anchor = "w")
label0.grid(row=0,column=0,sticky='W')
inFile = tk.StringVar()
inFile.set(u"فايل ورودي" )
entry0=tk.Entry(nb,textvariable=inFile)
entry0.grid(row=0,column=1,sticky='W')


def Open():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = "Select file",
                                          filetypes = (("CSV files","*.csv"),
                                                       ("all files","*.*")))
    inFile.set(filename)
    data=util.readcsv(inFile.get())
    choise=list(data)
    print(choise)
    menu1 = rainPop["menu"]
    menu1.delete(0, "end")
    menu2 = datePop["menu"]
    menu2.delete(0, "end")
    field1.set(choise[1])
    field2.set(choise[0])
    for string in choise:
        menu1.add_command(label=string,
                          command=lambda value=string: field1.set(value))
        menu2.add_command(label=string,
                          command=lambda value=string: field2.set(value))
btn1 = ttk.Button(nb,text="Open", style="C.TButton",command=Open)
btn1.grid(row=0,column=2,sticky='W')
##################
labelr = tk.Label(nb, text="Rain Field").grid(row = 1, column = 0)
choices = {"Select a Field"}
field1 = tk.StringVar()
rainPop= tk.OptionMenu(nb, field1, *choices)
rainPop.grid(row = 1, column =1)
field2 = tk.StringVar()
labeld=tk.Label(nb, text="Date Field").grid(row = 1, column = 2)
datePop = tk.OptionMenu(nb, field2, *choices)
datePop.grid(row = 1, column =3)
def change_field1(*args):
    print("You slected {} column as rain values".format( field1.get()))
field1.trace('w', change_field1)
def change_field2(*args):
    print("You slected {} column as date values".format( field2.get()))
field2.trace('w', change_field2)

##scale#############
label2= tk.Label(nb,text=u"گام زماني",fg="white",bg="blue")
label2.grid(row=2,column=0,sticky='W')

inScale = tk.StringVar()
entry2=tk.Entry(nb,textvariable=inScale)
entry2.grid(row=2,column=1,sticky='W')

def evaluate(event):
    print(inScale.get())
entry2.bind("<Leave>", evaluate)

######################
def onClick():
    scales1=[]
    inScale.set("")
    for key in chk:
        if   "var" in key :
            key=chk[key].get()
            scales1.append(key)
    scales1=sorted([int(i) for i in scales1 if str(i)])
    inScale.set(",".join([str(i) for i in scales1 ]))
    
scales=[1,3,6,9,12,24]
chk={}
k=0
for scale in scales:
    chk["var{}".format(scale)] = tk.StringVar()
    chk[str(scale)]= tk.Checkbutton(nb, text=str(scale),
                                    variable=chk["var{}".format(scale)],
                                    command=onClick,
                                    onvalue=str(scale), offvalue="")
    chk[str(scale)].grid(row=3,column=k)
    chk[str(scale)].deselect()
    k+=1

######output###########
label3= tk.Label(nb,text=u"فايل خروجي",fg="white",bg="blue")
label3.grid(row=4,column=0,sticky='W')

def Save():
    outfilename = filedialog.asksaveasfilename(initialdir = os.getcwd(),
                                               title = "Select Output file",
                                                filetypes = (("CSV files","*.csv"),("all files","*.*")))
    outFile.set(outfilename+".csv")

outFile = tk.StringVar()
outFile.set(u"فايل خروجي" )
entry3=tk.Entry(nb,textvariable=outFile)
entry3.grid(row=4,column=1,sticky='W' )
btn3= ttk.Button(nb,text="Save", style="C.TButton",
                 command=Save)
btn3.grid(row=4,column=2,sticky='W')

################
import spi
import util
def Calculate():
    data=util.readcsv(inFile.get())
    rain=data[field1.get()]
    dates=data[field2.get()]
    scales=list(map(int,inScale.get().split(",")))
    spivalues=spi.SPI(rain, dates ,scales).calculate(fit=util.gammafit)
    util.write(spivalues,outFile.get())
    print ('SPI is calcualted and saved in {}'.format(outFile.get()))
    
btn4= ttk.Button(nb,text="Calculate", style="C.TButton",
                 command=Calculate)
btn4.grid(row=5,column=1,sticky='W')
btn5= ttk.Button ( nb,text="Close", command=root.destroy)
btn5.grid(row=5,column=2,sticky='W')
###########################
menubar = tk.Menu(nb)
file = tk.Menu(menubar, tearoff = 2) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Open...', command = Open) 
file.add_command(label ='Save', command = Save) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)
root.config(menu=menubar)
##################
root.mainloop()
    
