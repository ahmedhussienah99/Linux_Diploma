from tkinter import *
import math


root=Tk()
root.geometry("300x400")
root.title("led")


def led_on():
    global state
    C.create_oval(60,60,210,210,fill="red")
    label1.configure(text="led is ON")



def led_off():
    C.create_oval(60,60,210,210,fill="white")
    label1.configure(text="led is OFF")


state="off"
C = Canvas(root, bg="White",height=250, width=300)
C.create_oval(60,60,210,210,fill="White")
C.pack()

label1 = Label(root, text='led is '+str(state))
label1.pack()



button1=Button(root,text="Led ON",command=led_on)
button1.pack()
button2=Button(root,text="Led OFF",command=led_off)
button2.pack()
root.mainloop()
