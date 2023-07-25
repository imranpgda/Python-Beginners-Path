import os
os.system('cls')

meas1=input("ENTER FIRST MEASURE [cm,mtr] >> ")
num=int(input("ENTER THE MEASURE VALUE >> "))
meas2=input("ENTER THE MEASURE YOU WANT [mm,in,ft,km,cm] >> ")

if(meas1=="cm"):
    if(meas2=="mm"):
       print(num,"cm =",num*10,"mm")
    elif(meas2=="in"):
         print(num,"cm =",num*0.39,"in")
    elif(meas2=="ft"):
        print(num,"cm =",num*0.0328,"ft")
    elif(meas2=="km"):
        print(num,"cm =",num*0.00001,"km")
    elif(meas2=="cm"):
        print(num,"cm =",num,"cm")
elif(meas1=="mtr"):
    if(meas2=="mm"):
       print(num,"mtr =",num*1000,"mm")
    elif(meas2=="in"):
         print(num,"mtr =",num*39,"in")
    elif(meas2=="ft"):
        print(num,"mtr =",num*3.28,"ft")
    elif(meas2=="km"):
        print(num,"mtr =",num*0.001,"km")
    elif(meas2=="cm"):
        print(num,"mtr =",num*100,"cm")

