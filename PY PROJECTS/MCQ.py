from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

#root 
root=Tk()
root.geometry("800x900")
root.title("CODE BONANJA")


#functions
def submit():
    list=[(var1.get()),(var2.get()),(var3.get()),(var4.get()),(var5.get())]
    print(list)
    anslist=[2,2,3,3,4]
    k=0
    res=0
   
    for i in list:
        if(i==anslist[k]):
            res+=2
        k+=1

    if(res>=3 and res<=6):
        messagebox.showinfo(title="Congratulation !",message=" You passed .")
    elif(res>6 and res<10):
        messagebox.showinfo(title="Congratulation !",message="Very good performance .")
    elif(res==10):
        messagebox.showinfo(title="Congratulation !",message="BHAYANKAR BHAI <>")




#variables:
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
#extend variable series when extend QUESTIONS <>


#Elements Q1<>
Label(root,bg="#ffcccb",text="Que1- Which one is the easiest programming language ?",font=('arial',11,BOLD)).grid(row=0,sticky=W)

Radiobutton(root,text="JAVA",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var1,value=1).grid(row=1)
Radiobutton(root,text="Python",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var1,value=2).grid(row=2)
Radiobutton(root,text="C++",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var1,value=3).grid(row=3)
Radiobutton(root,text="C",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var1,value=4).grid(row=4)

#code by IMRAN KHAN @imranpgda

#Elements Q2<>
Label(root,bg="#ffcccb",text="Que2- How many data types available in PYthon  ?",font=('arial',11,BOLD)).grid(row=5,sticky=W)

Radiobutton(root,text="2",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var2,value=1).grid(row=6)
Radiobutton(root,text="3",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var2,value=2).grid(row=7)
Radiobutton(root,text="4",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var2,value=3).grid(row=8)
Radiobutton(root,text="5",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var2,value=4).grid(row=9)



#Elements Q3<>
Label(root,bg="#ffcccb",text="Que3- How many types available in Literal Collection  ?",font=('arial',11,BOLD)).grid(row=10,sticky=W)

Radiobutton(root,text="3",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var3,value=1).grid(row=11)
Radiobutton(root,text="4",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var3,value=2).grid(row=12)
Radiobutton(root,text="5",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var3,value=3).grid(row=13)
Radiobutton(root,text="6",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var3,value=4).grid(row=14)



#Elements Q4<>
Label(root,bg="#ffcccb",text="Que4- Which one is the storage expression of the List  ?",font=('arial',11,BOLD)).grid(row=15,sticky=W)

Radiobutton(root,text="()",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var4,value=1).grid(row=16)
Radiobutton(root,text="{}",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var4,value=2).grid(row=17)
Radiobutton(root,text="[]",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var4,value=3).grid(row=18)
Radiobutton(root,text="--",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var4,value=4).grid(row=19)



#Elements Q5<>
Label(root,bg="#ffcccb",text="Que5- Which one is the correct command of If statement?",font=('arial',11,BOLD)).grid(row=20,sticky=W)

Radiobutton(root,text="else if",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var5,value=1).grid(row=21)
Radiobutton(root,text="if else if",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var5,value=2).grid(row=22)
Radiobutton(root,text="elif",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var5,value=3).grid(row=23)
Radiobutton(root,text="if else",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var5,value=4).grid(row=24)

#SUBMIT BUTTON <>
Button(root,text="SUBMIT",bg="lightgreen",font=('arial',15,BOLD),command=submit,bd=5,relief="sunken",pady=3).grid(row=25)


# #elements Q6<>
# Label(root,bg="#ffcccb",text="Que5- Which one is the correct command of to Print any statement?",font=('arial',11,BOLD)).grid(row=25)

# Radiobutton(root,text="printf()",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var6).grid(row=26)
# Radiobutton(root,text="cout>>()",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var6).grid(row=27)
# Radiobutton(root,text="print()",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var6).grid(row=28)
# Radiobutton(root,text="if else",bg="lightyellow",width=100,bd=5,font=('lucida',10),variable=var6).grid(row=29)



root.mainloop()