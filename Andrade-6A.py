#Kevin Andrade
#SE126.02
#February 21, 2022
#Lab 6A




def bsearch(name, list):
    
    min = 0
    max = len(last) -1
    guess = int((min + max ) / 2)
    while (name != list[guess] and min <= max):
        if (name < list[guess]):
            max = guess-1
        else: 
            min = guess + 1
        guess = int((min + max)/2)

    if(name == list[guess]):
        return guess
    else:
        return -1

def found(num,a,b,c,d,e,f):
    if(num == -1):
        print("\nEmployee Not Found In Records!")
    else:
        print("\nName: {0} {1}".format(a,b))
        print("Phone #: {0}".format(c))
        print("Email: {0}".format(d))
        print("Department: {0}".format(e))
        print("Position: {0}".format(f))
#========== Main Code ==========
import csv
from turtle import pos
frst = []
last = []
pnum = []
mail = []
dept = []
epos = []

with open("Lab6a-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for row in file:
        frst.append(row[0])
        last.append(row[1])
        pnum.append(row[2])
        mail.append(row[3])
        dept.append(row[4])
        epos.append(row[5])

searchName = input("Enter name: ")
position = bsearch(searchName, last)
found(position, frst[position], last[position], pnum[position], mail[position], dept[position], epos[position])


