import os 
os.system('cls')

col1=["Name","Age","Branch","Std Id","Phn Num"]
col2=[]

for i in col1:
    print("ENTER YOUR",i,">> ",end="")
    col2.append(input())
os.system('cls')
print("\n\nSHAMBHUNATH COLLEGE OF EDUCATION ")
print("==================================")
k=0
for i in col1:
    print("        ",i,"  :  ",col2[k])
    k+=1
    #by - IMRAN KHAN
print("==================================")

# OUTPUT >> 
# ENTER YOUR Name >> Imran Khan
# ENTER YOUR Age >> 19
# ENTER YOUR Branch >> Bca
# ENTER YOUR Std Id >> 22sbca0001
# ENTER YOUR Phn Num >> 7310351070


# SHAMBHUNATH COLLEGE OF EDUCATION 
# ==================================
#          Name   :   Imran Khan
#          Age   :   19
#          Branch   :   Bca
#          Std Id   :   22sbca0001
#          Phn Num   :   7310351070
# ==================================