import os

os.system("cls")

num=int(input("ENTER THE ROW NUMBER >> "))
#by - IMRAN KHAN
for i in range (1,num+1,1):
    for j in range (1,num+1,1):
        if(i==j or j==num+1-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()


#      OUTPUT FOR n=5

#       *   *
#        * * 
#         *  
#        * * 
#       *   *