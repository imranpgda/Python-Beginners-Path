import os
os.system('cls')

list=[]  #list empty declaration

len=int(input("ENTER THE LENGTH OF THE LIST YOU WANT >> "))
k=0
for i in range(len):
    list.append(int(input("ENTER THE ELEMENT >> ")))
    #append function for taking input

new=sorted(list)
#we can also use : list.sort() {But it will affect ORIGINAL list}
print("THE SORTED LIST IS >>> ",new)



# OUTPUT
# ENTER THE LENGTH OF THE LIST YOU WANT >> 5
# ENTER THE ELEMENT >> 43
# ENTER THE ELEMENT >> 00
# ENTER THE ELEMENT >> 5
# ENTER THE ELEMENT >> 3
# ENTER THE ELEMENT >> 8
# THE SORTED LIST IS >>>  [0, 3, 5, 8, 43]