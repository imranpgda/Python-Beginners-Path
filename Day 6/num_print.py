import os
os.system('cls')

#add of three number is if 10 then print this is low value and if add of between 10 and 15
#then print medium number and

num1= input("ENTER FIRST NUMBER >> ")
num2= input("ENTER SECOND NUMBER >> ")
num3= input("ENTER THIRD NUMBER >> ")

sum=int(num1)+int(num3)+int(num2)

if(sum<=10):
    print("THE NUMBER IS VERY LOW")
elif(sum>10 and sum<=15):
    print("THE NUMBER IS MEDIUM")
else:
    print("THE NUMBERS ARE HIGH ")