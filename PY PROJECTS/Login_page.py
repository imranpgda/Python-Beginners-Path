from tkinter import *
import os
from tkinter.font import BOLD
from tkinter import messagebox



#root options<>
root=Tk()
root.geometry("400x400")
root.configure(background="#41B3A3")

#FUNCTIONS<>
def submit():
    if((chekvar.get())!=1):
        messagebox.showinfo(title="HELLO !",message="BHAI .. Mujhe Tick Kar Pahle")

    namew=namevar.get()
    passw=passvar.get()
    if(namew=="imran" and passw=="1234"):
        messagebox.showinfo(title="WELCOME !",message="ACESS GRANTED .. Mr. IMRAN KHAN")
        
    else:
        messagebox.showwarning(title="WRONG PASSWORD",message="BHAI PASSWORD GALAT HAI >>") 
        passvar.set("")
        namevar.set("")




#DESIGN PHASE
Label(root,text="LOGIN PAGE",bg="#41B3A3",font=("lucida",15,BOLD)).pack(pady=20)
f1=Frame(root).place()
f2=Frame(root).pack()

#variables
namevar=StringVar()
passvar=StringVar()
chekvar=IntVar()

#elements<>
#1st term
Label(f1,text="USERNAME : ",bg="#41B3A3",font=("arial",10,BOLD)).place(x=30,y=70)
Entry(f1,textvariable=namevar,width=25,bg="#41B3A3",borderwidth=5,bd=5).place(x=130,y=70)


#2nd term
Label(f2,text="PASSWORD : ",bg="#41B3A3",font=("arial",10,BOLD)).place(x=30,y=110)
Entry(f2,textvariable=passvar,width=25,bg="#41B3A3",borderwidth=3,bd=5).place(x=130,y=110)


#button for Sumbmission
Button(root,text="SUBMIT",bg="#41B3A3",font=("arial",10,BOLD),command=submit,relief="groove").place(x=170,y=160)
#remember me button

rembbtn=Checkbutton(root,text="remember me ",bg="#41B3A3",activebackground="#41B3A3",borderwidth=3,font=("lucida",10),variable=chekvar,offvalue=0,onvalue=1).place(x=150,y=190)

root.mainloop()
