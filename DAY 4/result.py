import os 
#initialisation part
os.system('cls' if os.name == 'nt' else 'clear')


name=input("ENTER YOUR NAME >> ")
roll=input("ENTER YOUR ROLL NUMBER >> ")
std_id=input("ENTER YOUR STUDENT ID >> ")
hin_mark=input("\nENTER MARKS IN SUB- HINDI >> ")
eng_mark=input("ENTER MARKS IN SUB- ENGLISH >> ")
phy_mark=input("ENTER MARKS IN SUB- PHYSICS >> ")
chem_mark=input("ENTER MARKS IN SUB- CHEMISTRY >> ")
 

chs_sub=int(input("\nINPUT 1 for - BIOLOGY\nINPUT 2 for - MATHs\n"))

# def grade(x):
#    if(x > 90):
#       print("A+")
#    elif(x<90 and x>60): 
#       print("B+")
#    elif(x<60 and x>40):
#       print("C")
#    elif(x<40 and x>20):
#       print("fail")
   
def grade(x):
   std=''
   if(x > 90):
     std = "A+"
   elif(x<90 and x>60):
      std="B+"
                                 #program by IMRAN KHAN @imranpgda
   elif(x<60 and x>40):
      std="C"
   elif(x<40 and x>20):
      std="fail"
   return str(std)


if(chs_sub==1):
    last_sub=input("ENTER MARKS IN BIOLOGY >> ")
    last_subject=1
elif(chs_sub==2):
    last_sub=input("ENTER MARKS IN SUBJECT - MATHs >>")
    last_subject=2

#calculation part
os.system('cls' if os.name == 'nt' else 'clear')




total=500
sum=int(hin_mark)+int(eng_mark)+int(phy_mark)+int(chem_mark)+int(last_sub)
#sum=float(hin_mark)+float(eng_mark)+float(phy_mark)+float(chem_mark)+float(last_sub)

#representation part



print("\n")
print("              SHAMBHUNATH COLLEGE OF EDUCATION        ")
print("                   RESULT SESSION 2023-24             \n")
print(" =================================================================== ")
print("                                          STUDENT NAME : ",name)
print("                                          STUDENT ROLL NUMBER :",roll)
print("                                          STUDENT ID : ",std_id)
print(" =================================================================== ")
print("  SUBJECTS                 ||        MARKS      ||  GRADE")
print(" ------------------------------------------------------------------- ")
print("   HINDI                   ||        ",hin_mark,"       ||  ",grade(int(hin_mark)))
print("   ENGLISH                 ||        ",eng_mark,"       ||  ",grade(int(eng_mark)))


print("   PHYSICS                 ||        ",phy_mark,"       ||  ",grade(int(phy_mark)))
print("   CHEMISTRY               ||        ",chem_mark,"       ||  ",grade(int(chem_mark)))
if(last_subject==1):
  print("   BIOLOGY                 ||        ",last_sub,"       ||  ",grade(int(last_sub)))
elif(last_subject==2):
  print("   MATHs                   ||        ",last_sub,"       ||  ",grade(int(last_sub)))
print(" ------------------------------------------------------------------- ")
print("                                            TOTAL MARKS : ",total)
print("                                            MARKS OBTAINED :",sum,"/",total)
print("                                            TOTAL MARKS(%) : ",float(sum/5),"%")

print("| =================================================================== |")
print("|   Board Sign.______________     ||    Principle Sign.____________   |")
print("| =================================================================== |")

