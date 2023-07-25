import os
os.system('cls')

col1=["Name","DOB","Father's Name","Mother's Name","<< Qualifications >>"]
col2=[]
qual=[]

for i in col1[0:-1]:
    print("ENTER YOUR",i,">> ",end="")
    col2.append(input())
#CODE BY - IMRAN KHAN @imranpgda
qual_range=int(input("\nENTER HOW MUCH QUALIFICATIONS DO YOU HAVE >> "))

#QUALIFICATION LIST >> INPUT
for i in range (qual_range):
    print("ENTER YOUR",col1[-1],">> ",end="")
    qual.append(input())

os.system('cls')
k=0
#PRINTING TOP HEAD >>
for i in col1[0:-1]:
    print(" ",i," : ",col2[k])
    k+=1
#PRINTIG QUALIFICATION >>
print("      ",col1[-1],":")
for i in qual:
   print("     <> ",i)
#SKILLS LIST
skills_s=["<< Skills & Certificates >>","Java","C","Html","Css","JavaScript","Design Thinking","UI/UX","FireBase","Git/GitHub","Python"]
#PRINTING SKILLS LIST >>
print(skills_s[0],":\n")
for i in skills_s[1:]:
    print(   "-",i)
#ABOUT ME SECTION >>
aboumee="I am a highly motivated and enthusiastic BCA student seeking an internship opportunity to gain practical experience & enhancemy skills in the field of software technologies.\n My strong academic background & passion for technology have equipped me with a solid foundation in programming languages such as JAVA, C, Python, Html & CSS .\n My interested fields are Android Development & Web Development."

print("\n<><> ABOUT ME <><>\n",aboumee)
print("\n")
print("<><> CONTACT ME <><>\n")
#CONTACT LIST 
cont_act=["Email","Phn num","Address","LinkedIn","Instagram"]
cont_info=["imranpgda@gmail.com","+91 7310351070","Jhalwa,Prayagraj","@imranpgda","@imranpgda"]
k=0
#CONTACT PRINTING >>
for i in cont_act:
    print("                            ",i," : ",cont_info[k])
    k+=1