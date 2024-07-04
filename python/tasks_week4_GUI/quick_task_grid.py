import tkinter as tk

root=tk.Tk()
root.geometry("500x500")
root.title("grid")

button1=tk.Button(root,text="button1")
button1.grid(row=0,column=1)
button2=tk.Button(root,text="button2")
button2.grid(row=1,column=0)
button3=tk.Button(root,text="button3")
button3.grid(row=1,column=3)
button4=tk.Button(root,text="button4")
button4.grid(row=2,column=1)
root.mainloop()

