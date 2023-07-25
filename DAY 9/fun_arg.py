import time
import os

os.system('cls')
t=(time.gmtime().tm_hour)
name=input("ENTER YOUR NAME >> ")

if(t>=1 and t<=6):
    print("HELLO Mr.",name+" GOOD MORNING SIR !")
elif(t>6 and t<=10):
    print("HELLO Mr.",name+" GOOD AFTERNOON SIR !")
elif(t>10 and t<12):
    print("HELLO Mr.",name+" GOOD EVENING SIR !")
elif(t>12 and t<=24):
    print("HELLO Mr.",name+" GOOD NIGHT SIR !")