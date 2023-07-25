from tkinter import *
root = Tk()
def test():
    print("hello ")
pic=PhotoImage(file="Screenshot 2023-07-11 105609.png")

btn1=Button(root,image=pic,command=test).pack()


root.mainloop()
