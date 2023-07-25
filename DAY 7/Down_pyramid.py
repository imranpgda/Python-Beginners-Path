import os

os.system("cls")

num=int(input("ENTER THE ROW NUMBER >> "))
#by - IMRAN KHAN
for i in range (num+1,0,-1):
    for j in range (i,0,-1):
        print("*",end="")
    print()

#   OUTPUT

#   ENTER THE ROW NUMBER >> 5

#   ******
#   *****
#   ****
#   ***
#   **
#   *