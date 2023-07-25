import csv

csvfile=open('persons.csv','r',newline='')
obj=csv.reader(csvfile)

for row in obj:
    print (row)
