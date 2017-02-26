from randgen import generate_randinput
import csv
from girl import girl
from boy import boy

generate_randinput()
     
girll = []
boi = []
with open('girlie.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    
    for row in readCSV:
       girll.append(girl(row[0],(int)(row[1]),(int)(row[2]),(int)(row[3])))
        
with open('boy.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    
    for row in readCSV:
       boi.append(boy(row[0],(int)(row[1]),(int)(row[2]),(int)(row[3]),(int)(row[4])))
print len(girll),len(boi)
##instances created


pair = {}
for a in girll:
    for b in boi:
        if(b.budget>=a.maintainence_budget and b.attraction_requirement<=a.attractiveness and b.status == a.status == 0):
            pair.update({a.name:b.name})
            a.status = 1
            b.status = 1

for a in girll:
    if a.status == 0:
        print a.name+" is single"
    else:
        print a.name+"->"+pair[a.name]
                  

                    
            



