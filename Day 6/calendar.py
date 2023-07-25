import os
os.system('cls')

mon=input("Enter Month Name's First Three Letter  as(feb) >> ")
day=input("Enter Day Count Number >> ")

def day_name(x):
    dayname=''
    if(x==1):
        dayname="Sunday"
    elif(x==2):
         dayname="Monday"
    elif(x==3):
         dayname="Tuesday"
    elif(x==4):
         dayname="Wednesday"
    elif(x==5):
         dayname="Thursday"
    elif(x==6):
         dayname="Friday"
    elif(x==7):
         dayname="Saturday"
    if(x>7):
         if(x%7==1):
            dayname="Sunday"
         elif(x%7==2):
            dayname="Monday"
         elif(x%7==3):
             dayname="Tuesday"
         elif(x%7==4):
            dayname="Wednesday"
         elif(x%7==5):
            dayname="Thursday"
         elif(x%7==6):
           dayname="Friday"
         elif(x%7==7):
            dayname="Saturday"
         return dayname
    

if(mon=="jan"):
    print("The Day Was",day_name(int(day)),"At",day,"JANUARY")
elif(mon=="feb"):
   print("The Day Was",day_name(int(day)),"At",day,"FEBRUARY")
elif(mon=="mar"):
   print("The Day Was",day_name(int(day)),"At",day,"MARCH")
elif(mon=="apr"):
   print("The Day Was",day_name(int(day)),"At",day,"APRIL")
elif(mon=="may"):
   print("The Day Was",day_name(int(day)),"At",day,"MAY")
elif(mon=="jun"):
   print("The Day Was",day_name(int(day)),"At",day,"JUNE")
elif(mon=="jul"):
   print("The Day Was",day_name(int(day)),"At",day,"JULY")
elif(mon=="aug"):
   print("The Day Was",day_name(int(day)),"At",day,"AUGUST")
elif(mon=="sep"):
   print("The Day Was",day_name(int(day)),"At",day,"SEPTEMBER")
elif(mon=="oct"):
   print("The Day Was",day_name(int(day)),"At",day,"OCTOBER")
elif(mon=="nov"):
   print("The Day Was",day_name(int(day)),"At",day,"NOVEMBER")
elif(mon=="dec"):
   print("The Day Was",day_name(int(day)),"At",day,"DECEMBER")
