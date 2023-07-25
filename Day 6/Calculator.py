import os
os.system('cls')

num1=input("ENTER FIRST NUMBER >> ")
chs=input("ENTER THE OPERATION >> ")
num2=input("ENTER SECOND NUMBER >> ")

if(chs=="+"):
    print("SUM OF",num1,"+",num2,"=",int(num1)+int(num2))
elif(chs=="-"):
    print("SUB OF",num1,"+",num2,"=",int(num1)-int(num2))
elif(chs=="*"):
    print("SUB OF",num1,"+",num2,"=",int(num1)*int(num2))
elif(chs=="/"):
  print("SUB OF",num1,"+",num2,"=",int(num1)/int(num2))
