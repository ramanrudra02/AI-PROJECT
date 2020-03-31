from tkinter import Toplevel, Button, Tk, Menu
from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry('1000000x10000000')
def getvals():
    messagebox.showinfo('USERNAME',uservalue.get())

    messagebox.showinfo('PASSWORD',passwordvalue.get())


msg = Message(top, text="WELCOME TO",width=5000,font=('arial',22))
msg.config(bg='green')
msg.pack()
menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit", command=top.quit)

menubar.add_cascade(label="File", font=('arial',15),menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)





f1=LabelFrame(top,text="TV SHOW POPULARITY ANALYSIS",font=('arial','25','bold italic'),bd=5,borderwidth=10,relief=RAISED)
f1.pack(side=LEFT,fill=BOTH,expand=1)


user=Label(f1,text="USERNAME",font='25',width='10',height='2').grid(row=0,column=1)
password=Label(f1,text="PASSWORD",font='25',width='10',height='2').grid(row=1,column=1)
uservalue=StringVar()
passwordvalue=StringVar()


ue=Entry(f1,textvariable=uservalue,width='20',font=('arial',15)).grid(row=0,column=2)
pe=Entry(f1,textvariable=passwordvalue,width='20',font=('arial',15),show="*").grid(row=1,column=2)

b1=Button(f1,text='submit',command=getvals,relief=RAISED,font=('arial',15)).grid(row=2,column=2)

top.config(menu=menubar)
top.mainloop()
