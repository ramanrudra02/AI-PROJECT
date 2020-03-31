from tkinter import*
import os
import sqlite3

root=Tk()
display = Label(root)
root.configure(bg='light green')
root.title("LOGIN PAGE")
root.geometry('900x500')
Email=StringVar()
Password=StringVar()  
email=Email.get()
password=Password.get()
       def tv():
        database1()

        root=Tk()
        root.geometry("1600x8000")
        root.title("CHANNELS")
        root.configure(bg='light green')
        
   NAME= StringVar()

        def additem(*args):
            with open('test.txt', 'a+') as f:
               f.write(NAME.get()+'\n')
               f.write("\n")           Label(root,text="Email",bg="light green", font=('times new roman', 20,"bold")).place(x=100,y=100)
Entry(root,textvar=Email,bg="goldenrod",bd=10, font=('times new roman', 20,"bold")).place(x=300,y=100)
Label(root,text="Password",bg="light green", font=('times new roman', 20,"bold")).place(x=100,y=200)
Entry(root,textvar=Password,bg="goldenrod",bd=10, font=('times new roman', 20,"bold")).place(x=300,y=200)
Button(root,text="Submit",bg="light green",bd=10, font=('times new roman', 20,"bold"),command=t
