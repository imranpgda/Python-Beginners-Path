from tkinter import *
from tkinter.font import BOLD

#ROOT SECTION<>
root=Tk()
root.geometry('300x300')
root.title("RADIO-BUTTON")

#func
def register():
    x=rvar.get()
    if(x==1):
        print("MALE")
    elif(x==2):
        print("FEMALE")
    else:
        print("OTHERS")

#Label 
rvar=IntVar()

# RADIOBUTTON

rd1=Radiobutton(root,text="1- MALE ",variable=rvar,font=("lucida",15,BOLD),value=1).pack(anchor=W)
rd2=Radiobutton(root,text="2- FEMALE ",variable=rvar,font=("lucida",15,BOLD),value=2).pack(anchor=W)
rd3=Radiobutton(root,text="3- OTHERS ",variable=rvar,font=("lucida",15,BOLD),value=3).pack(anchor=W)
regbtn=Button(root,text="SUBMIT",font=("lucida",15,BOLD),bd=5,command=register).pack(anchor=W)
root.mainloop()
