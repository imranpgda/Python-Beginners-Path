import os
os.system("cls")

def countdig(x):
    count=0
    while(x!=0):
        x=x/10
        rem=x%10
        if(rem>0):
            count+=1
    return (count)

num=int(input("ENTER THE NUMBER >> "))
temp=num
sum=0

print("DIGIT OF THE NUMBERS ARE >> ",countdig(num))
while(num!=0):
    num=num/10
    rem=num%10
    sum=sum+(rem**2)
    
print(sum)
if(sum==num):
    print(temp,"IS AN ARMSTRONG NUMBER <>")
else:
    print(temp,"IS NOT AN ARMSTRONG NUMBER >> ")


