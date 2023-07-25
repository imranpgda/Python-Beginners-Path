import os

os.system("cls")

num=int(input("ENTER THE ROW NUMBER >> "))
#by - IMRAN KHAN
for i in range (num):
    for j in range (i+1):
        print("*",end="")
    print()


#      OUTPUT:

#      ENTER THE ROW NUMBER >> 5

#      *
#      **
#      ***
#      ****
#      *****