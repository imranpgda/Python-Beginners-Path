import os

os.system("cls")

num=int(input("ENTER THE NUMBER >> "))
a=0
b=1
sum=0
#by - IMRAN KHAN
print("FIBONACCI SERIES IS >> ",end="")
for i in range (num):
    print(sum," ",end="")
    sum=a+b
    b=a
    a=sum


# OUTPUT: 

# ENTER THE NUMBER >> 10
# FIBONACCI SERIES IS >> 0  1  1  2  3  5  8  13  21  34  
