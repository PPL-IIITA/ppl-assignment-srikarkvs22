import csv
import random
from random import randint

def generate_randinput():
    g = []
    for i in range(1,51):
        g.append(('Girl'+str(i),random.randint(1,11),random.randint(1,11),random.randint(1,50000),random.randint(1,11)))
    f = open('girlie.csv',"w")
    w = csv.writer(f,delimiter = ',')
    for i in g:
        w.writerow(i)
    f.close    
    b = []
    for i in range(1,1001):
        b.append(('Boy'+str(i),random.randint(1,11),random.randint(1,11),random.randint(1,50000),random.randint(1,11)))
    f = open('boy.csv',"w")
    w = csv.writer(f,delimiter = ',')
    for i in b:
        w.writerow(i)
    f.close

