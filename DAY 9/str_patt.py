import os
os.system("cls")

name=input("ENTER THE STRING >> ")
print()

for i in range(len(name)):
    for j in range (i+1):
        print(name[j],"",end="")
    print()

print()