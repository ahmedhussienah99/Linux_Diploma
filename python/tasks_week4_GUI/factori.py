from tkinter import *
import math


root=Tk()
root.geometry("300x300")
root.title("Reverse String")


def claculate_func():
    x=0
    global v3
    global radio1
    global radio2

    op1=int(entry1.get())
    op2=math.factorial(op1)
    label3 = Label(root, text='the Reverse String is : '+str(op2))
    label3.grid(row=30,column=50)  



 


v1=StringVar()


label1 = Label(root, text='Enter a Word')
label1.grid(row=0,column=0)
entry1=Entry(root,width=20,textvariable=v1)
entry1.grid(row=0,column=50)


button1=Button(root,text="Validate",command=claculate_func)
button1.grid(row=5,column=50)

root.mainloop()
