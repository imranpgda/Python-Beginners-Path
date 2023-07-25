from tkinter import *
from tkinter.font import BOLD
root = Tk()

#ROOT SIZE:
root.minsize(height=300,width=300)
root.maxsize(height=310,width=310)
root.title("CALCULATOR")
root.resizable=(False,False)
root.configure(background="#17161b")


#FUNCTIONS HERE >>
equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calc():
    global equation
    result=""
    if(equation!=""):
        try:
            result=eval(equation)
            equation=""
        except:
            result="<>error<>"
            equation=""
    label_result.config(text=result)



#TEXT SHOW <> LABEL 
label_result=Label(root,width=15,text="",font=("arial",30))
label_result.pack(ipadx=10,padx=5,pady=5)


#### PROGRAM BY IMRAN KHAN @imranpgda


#DIV > FRAME > BUTTONS
f=Frame(root,width=100,bg="grey")
f.pack()


#MAIN BUTTONS >> C F G
bcl=Button(f,width=5,bg="#3697f5",text="C",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : clear()).grid(row=0,column=0)
bmod=Button(f,width=5,bg="#2a2d36",text="%",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("%")).grid(row=0,column=1)
bdev=Button(f,width=5,bg="#2a2d36",text="/",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("/")).grid(row=0,column=2)

#BUTTONS >> DIV 1
b7=Button(f,width=5,bg="#2a2d36",text="7",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("7")).grid(row=1,column=0)
b8=Button(f,width=5,bg="#2a2d36",text="8",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("8")).grid(row=1,column=1)
b9=Button(f,width=5,bg="#2a2d36",text="9",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("9")).grid(row=1,column=2)
#row2
b4=Button(f,width=5,bg="#2a2d36",text="4",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("4")).grid(row=2,column=0)
b5=Button(f,width=5,bg="#2a2d36",text="5",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("5")).grid(row=2,column=1)
b6=Button(f,width=5,bg="#2a2d36",text="6",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("3")).grid(row=2,column=2)
#row3
b1=Button(f,width=5,bg="#2a2d36",text="1",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("1")).grid(row=3,column=0)
b2=Button(f,width=5,bg="#2a2d36",text="2",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("2")).grid(row=3,column=1)
b3=Button(f,width=5,bg="#2a2d36",text="3",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("3")).grid(row=3,column=2)
#row4
b0=Button(f,width=5,bg="#2a2d36",text="0",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("0")).grid(row=4,column=0)
b00=Button(f,width=5,bg="#2a2d36",text="00",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("00")).grid(row=4,column=1)
bdot=Button(f,width=5,bg="#2a2d36",text=".",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show(".")).grid(row=4,column=2)
#OPERATORS>
bequal=Button(root,width=5,height=3,bg="#fe9037",text="=",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : calc()).place(x=232,y=205)
bsum=Button(f,width=5,bg="#2a2d36",text="+",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("+")).grid(row=2,column=4)
bsub=Button(f,width=5,bg="#2a2d36",text="-",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("-")).grid(row=1,column=4)
bmul=Button(f,width=5,bg="#2a2d36",text="*",font=("Arial",15,BOLD),bd=1,fg="#fff",padx=5,pady=5,command=lambda : show("x")).grid(row=0,column=4)


root.mainloop()