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

