import csv

persons=[('lata',22,45),('anil',21,43),('imran',19,19)]
csvfile=open('persons.csv','w',newline='')

obj=csv.writer(csvfile)

for person in persons:
    obj.writerow(person)


csvfile.close()