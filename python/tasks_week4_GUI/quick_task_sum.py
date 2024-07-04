from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("sum")


def claculate_func():
    x=0
    global v3
    global radio1
    global radio2

    op1=entry1.get()
    op2=entry2.get()

    if(v3.get()==1):
        x=int(op1)-int(op2)
        label3 = Label(root, text='the'+"sub"+"is :"+str(op1)+"+"+str(op2)+"="+str(x))
        label3.grid(row=30,column=50)  

    if(v3.get()==2):
        x=int(op1)+int(op2)
        label3 = Label(root, text='the'+"sum"+"is :"+str(op1)+"+"+str(op2)+"="+str(x))
        label3.grid(row=30,column=50)
        #radio2.deselect()/.destory

 


v1=StringVar()
v2=StringVar()


label1 = Label(root, text='Enter the value of M')
label1.grid(row=0,column=0)
entry1=Entry(root,width=20,textvariable=v1)
entry1.grid(row=0,column=50)

label2 = Label(root, text='Enter the value of N')
label2.grid(row=1,column=0)
entry2=Entry(root,width=20,textvariable=v2)
entry2.grid(row=1,column=50)

v3=IntVar()
radio1=Radiobutton(root,text='sub',variable=v3,value=1)
radio1.grid(row=55,column=0)
radio2=Radiobutton(root,text='sum',variable=v3,value=2)
radio2.grid(row=56,column=0)

button1=Button(root,text="Validate",command=claculate_func)
button1.grid(row=60,column=50)

root.mainloop()
