import os
os.system('cls')

k=0
a=()
sub=("HINDI","ENGLISH","MATH","PHYSICS","CHEMISTRY")
for i in sub:
    print("ENTER",sub[k],"MARKS >> ",end="")
    a+=int(input())
    k+=1
#by - IMRAN KHAN
k=0
for i in a:
      print("        ",sub[k],"  :  ",i)
      k+=1
    #by - IMRAN KHAN