import os

os.system("cls")

#by - IMRAN KHAN
a=int(input("ENTER THE NUMBER >> "))
b=int(input("ENTER SECOND NUMBER >> "))
sum=0
if(b<=a):
    print("PLEASE ENTER BIGGER VALUE OF B THAN A <>")
else:
    for i in range (a,b+1,1):
         sum=sum+i
         if(i!=b):
           print(i,"+ ",end="")
         else:
            print(b,"=",sum)
       