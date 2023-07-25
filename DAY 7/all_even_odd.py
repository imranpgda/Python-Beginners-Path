import os

os.system("cls")

num=int(input("ENTER THE LAST NUMBER >> "))
#by - IMRAN KHAN
for i in range (1,num+1,1):
    if(i%2==0):
        print("EVEN : ",i)
   
for i in range (1,num+1,1):
    if(i%2!=0):
        print("ODD : ",i)
  
  
#   OUTPUT for n=5
#   EVEN :  2
#   EVEN :  4
#   ODD :  1
#   ODD :  3
#   ODD :  5