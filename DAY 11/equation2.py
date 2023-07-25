import os
os.system("cls")
x=int(input("ENTER VALUE OF X >> "))
y=int(input("ENTER VALUE OF Y >> "))
eval = lambda a,b:(a**3)+(17*a*b)+(b**2)
print("x^3 + 17xy + y^2 = ",eval(x,y))