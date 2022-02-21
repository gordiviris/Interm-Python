#Kevin Andrade
#SE126.02
#February 15, 2022
#Lab 5B

#---------- Functions ----------
def findDept(list):
    '''Goes through each employees deptartment and saves list position into a list'''
    pos = []
    length = len(list)
    for x in range (0,length):
        if list[x] == "MIS":
            pos.append(x)
    return pos

def comToNet(a,b):
    '''goes through list from finddept fuction and changes every email in those positions from "com" to ".net" '''
    length = len(a)
    for x in range (0,length):
        b[a[x]] = b[a[x]].replace("com","net")
        #print(b[a[x]])





#========== Main Code ==========
import csv

#initializing lists
frst = []
last = []
pnum = []
mail = []
dept = []
epos = []


with open("Lab5B.csv") as csvfile: #importing file and saves each value into respective list
    file = csv.reader(csvfile)
    for row in file:
        frst.append(row[0])
        last.append(row[1])
        pnum.append(row[2])
        mail.append(row[3])
        dept.append(row[4])
        epos.append(row[5])

misDept = findDept(dept) #sending dept list to function
#print(misDept)
comToNet(misDept, mail)
numChange = len(misDept) #amount of emails changed in the list
print(numChange,"Emails were changed") #displays # of emails changed 
 
#for x in range (0,len(mail)):
#    print(mail[x])

