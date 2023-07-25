import os
os.system("cls")


num=int(input("ENTER THE NUMBER YOU WANT CUBE OF >> "))

# def cube(x):
#     return x**3

#lambda func
cube=lambda x :x**3  

print(num,"^3"," = ",cube(num))