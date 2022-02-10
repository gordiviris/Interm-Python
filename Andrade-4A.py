#Kevin Andrade
#SE126.02
#January 31, 2022
#Lab 4A

#Variable Dictionary

#ram8     counter for how many 8gb systems there are
#current  gets last position of nList
#tList    Desktops or Laptops in a list
#bList    list of brands
#cList    list of CPU's
#rList    list of Ram Sizes
#h1List   list of size of 1st drive
#nList    number of drives in the system
#h2List   list of size of secon drives
#oList    list of OS
#yList    list of Years purchased
#length   length of rList


#========== Main Code ==========
import csv

#Initializing counter and all list
ram8 = 0
tList = []
bList = []
cList = []
rList = []
h1List = []
nList = []
h2List = []
oList = []
yList = []

with open("C:\\Users\\andra\\OneDrive\\Desktop\\PYTHON SE126\\lab4a.csv") as csvfile:
    lab4a = csv.reader(csvfile)

    for row in lab4a:
        tList.append(row[0])    #adding each row into appropriate lists
        bList.append(row[1])
        cList.append(row[2])
        rList.append(row[3])
        h1List.append(row[4])
        nList.append(row[5])

        current = len(nList) - 1    #Gets length of current size of nlist, subtracts one to stay in range

        if (nList[current] == "1"): #if statement to check if system has 1 or 2 drives
            oList.append(row[6])
            yList.append(row[7])
            h2List.append("")
        else:
            h2List.append(row[6])
            oList.append(row[7])
            yList.append(row[8])

length = len(rList) #final length of rLists

for x in range (0, length): #for loop to run through every item in rList
    if rList[x] == "08":    #checks each item in rList for "08" meaning 8 gb of ram and adds one to counter 
        ram8 += 1
print("NUmber of PC's with 8 GB of Ram: ",ram8) #output