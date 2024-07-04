from tkinter import *

#you should pass value argment for scale entity 
def priu(value):
    global t3
    global line1
    C.delete(t3)
    C.delete(line1)
    t3 = C.create_text(150, 150,font="Times 12 bold",text=str(v.get()))
    x=2.4*int(v.get())
 

    line1 = C.create_line(x, 100,150, 150,fill="green")

    #print(value,v.get())

root=Tk()
root.geometry("300x300")
root.title("Guage")

v=IntVar()


C = Canvas(root, bg="White",height=250, width=300)
arc1 = C.create_arc(0, 100, 300,50, start=0,extent=160,outline="green",style="arc",width=40)
arc2 = C.create_arc(0, 100, 300,50, start=0,extent=60,outline="yellow",style="arc",width=40)
arc3 = C.create_arc(0, 100, 300,50, start=0,extent=40,outline="red",style="arc",width=40)
t1 = C.create_text(20, 100,font="Times 12 bold",text="0")
t2 = C.create_text(280, 100,font="Times 12 bold",text="100")

t3 = C.create_text(150, 150,font="Times 12 bold",text=str(v.get()))
#line from 30 to 270 step=(270-30)/100-0=2.4
#coord of x equal step*angle
line1 = C.create_line(30, 100,150, 150,fill="green")
C.pack()
s = Scale(root, from_=0, to=100,variable=v, orient=HORIZONTAL,command=priu)
s.pack()





root.mainloop()
