import os
os.system("cls")

count=0
num=int(input("ENTER THE NUMBER >> "))
#by - IMRAN KHAN
for i in range (1,num+1,1):
    if(num%i==0):
        count+=1

if(count>2):
    print("THE NUMBER ",num,"IS NOT A PRIME NUMBER ")
else:
    print("THE NUMBER ",num,"IS A PRIME NUMBER ")


#     OUTPUT 1
#     ENTER THE NUMBER >> 7
#     THE NUMBER  7 IS A PRIME NUMBER 

#     OUTPUT 2
#     ENTER THE NUMBER >> 10
#     THE NUMBER  10 IS NOT A PRIME NUMBER 
