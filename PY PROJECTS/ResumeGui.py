from tkinter import *
import os
from tkinter.font import BOLD
os.system('cls')

#root
root=Tk()
root.geometry('700x800')
root.title("RESUME FORMAT >> ")
root.resizable(False,False)

#Functions>>
def register():
    name=namevar.get()
    mname=mnamevar.get()
    fname=fnamevar.get()
    dob=dobvar.get()
    age=agevar.get()
    dob=dobvar.get()
    cont=contvar.get()
    chekbox=chekvar.get()

    


#div > frames
# topdiv=Frame(root,bg="#FBFBFB",width=100).pack()
# middiv=Frame(root,bg="#000000",width=100).pack()

#labels for showing>>
Toplabel=Label(root,text="ENTER YOUR DETAILS HERE",font=("lucida",20,BOLD)).pack(side="top")

name=Label(root,text="NAME-",font=("arial",10,BOLD)).place(x=50,y=100)
Mothername=Label(root,text="Mother's Name-",font=("arial",10,BOLD)).place(x=50,y=130)
Fathername=Label(root,text="Father's Name-",font=("arial",10,BOLD)).place(x=50,y=160)
age=Label(root,text="Age-",font=("arial",10,BOLD)).place(x=50,y=190)
dob=Label(root,text="D.O.B-",font=("arial",10,BOLD)).place(x=50,y=220)
Contact=Label(root,text="Contact-",font=("arial",10,BOLD)).place(x=50,y=250)

#STRING_VARIABLES<>
namevar=StringVar()
mnamevar=StringVar()
fnamevar=StringVar()
agevar=StringVar()
dobvar=StringVar()
contvar=StringVar()
chekvar=IntVar()


#ENTRY FOR ENTERING DATA >> 
nameEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=namevar).place(x=170,y=100)
mnameEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=mnamevar).place(x=170,y=130)
fnameEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=fnamevar).place(x=170,y=160)
ageEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=agevar).place(x=170,y=190)
dobEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=dobvar).place(x=170,y=220)
contEn=Entry(root,width=25,font=("lucida",15),bd=3,textvariable=contvar).place(x=170,y=250)



#buttons<>
rembbtn=Checkbutton(root,text="remember me ",font=("lucida",10),variable=chekvar).place(x=170,y=300)
regbtn=Button(root,text="Submit",bd=4,font=("arial",15,BOLD),command=register).place(x=250,y=330)

#LABELS FOR DATA SHOW >>
nameshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=namevar,font=('lucida',15,BOLD)).place(x=200,y=390)
mnameshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=mnamevar,font=('lucida',15,BOLD)).place(x=200,y=430)
fnameshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=fnamevar,font=('lucida',15,BOLD)).place(x=200,y=470)
dobshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=dobvar,font=('lucida',15,BOLD)).place(x=200,y=510)
ageshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=agevar,font=('lucida',15,BOLD)).place(x=200,y=550)
contshow=Label(root,width=20,bg='lightyellow',bd=5,textvariable=contvar,font=('lucida',15,BOLD)).place(x=200,y=590)


root.mainloop()