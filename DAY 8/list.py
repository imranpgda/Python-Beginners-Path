import os
os.system('cls')

num=int(input("ENTER THE LIST LENGTH >> "))

a=[]
for i in range(num):
    a.append(input("ENTER THE ELEMENT  >> "))
#by - IMRAN KHAN
print("\n||  THE LIST IS  ||")
for i in a:
    print(i)

# OUTPUT>>
# ENTER THE LIST LENGTH >> 5
# ENTER THE ELEMENT  >> Imran
# ENTER THE ELEMENT  >> 5632
# ENTER THE ELEMENT  >> 22Sbca132
# ENTER THE ELEMENT  >> 543
# ENTER THE ELEMENT  >> 44

# ||  THE LIST IS  ||
# Imran
# 5632
# 22Sbca132
# 543
# 44