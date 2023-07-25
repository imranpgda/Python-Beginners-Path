import os

os.system("cls")

num=int(input("ENTER THE LAST NUMBER >> "))
sum=0
#by - IMRAN KHAN
for i in range (1,num+1,1):
    sum=sum+i
    if(i==num):
        print(num,"=",sum)
    else:
        print(i,"+ ",end="")


    
#      OUTPUT FOR n=5
#      1 + 2 + 3 + 4 + 5 = 15