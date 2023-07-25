import os

os.system("cls")

num=int(input("ENTER THE ROW NUMBER >> "))
#by - IMRAN KHAN
for i in range (1,num+1,1):
    for j in range (1,num+1,1):
        if(i==1 or i==num or j==1 or j==num):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# OUTPUT
#         *****
#         *   *
#         *   *
#         *   *
#         *****