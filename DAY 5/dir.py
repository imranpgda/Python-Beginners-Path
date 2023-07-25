import os

os.system('cls')

dir1=input("ENTER DISTANCE COVERED IN FRONT DIRECTION >> ")
if(int(dir1)>10):
     print("\n<< YOU NEED TO TAKE A REST >> ")
else:
  dir2=input("ENTER DISTANCE COVERED IN BACKWARD DIRECTION >> ")
  if(int(dir1)+int(dir2)>10):
    print("\n<< YOU NEED TO TAKE A REST >> ")
  else:
    dir3=input("ENTER DISTANCE COVERED IN LEFT DIRECTION >> ")
    if(int(dir1)+int(dir2)+int(dir3)>10):
      print("\n<< YOU NEED TO TAKE A REST >> ")
    else:
      dir4=input("ENTER DISTANCE COVERED IN RIGHT DIRECTION >> ")
      if(int(dir1)+int(dir2)+int(dir3)+int(dir4)>10):
         print("\n<< YOU NEED TO TAKE A REST >> ")
      else:
         print("\n<< YOU CAN STILL RUN SOME MORE >> ")

        
