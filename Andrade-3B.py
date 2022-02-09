#Kevin Andrade
#SE126.02
#January 25, 2022
#Lab 3B

#Variable Dictionary

#counter   counter of rows in file
#file      holds all file info.
#type      desktop or laptop
#tList     stores if pc is a Desktop or Laptop
#bList     stores brand of PC
#cpuList   stores cpu of PC
#ramList   amount of ram in PC
#h1List    amount of storage on 1st Disk
#hddList   num of Disk in the system
#h2List    amount of storage on 2nd Disk
#osList    operating system on PC
#yrList    list of years of PC's
#yr        year of PC 
#current   current year
#desktop   number of desktops to be replaced
#laptop    number of laptops to be replaced
#dcost     cost to replace desktops
#lcost     cost to replace laptops
#========== Main Code ==========

import csv

counter = 0
current = 22
desktop = 0
laptop = 0
lcost = 1500
dcost = 2000
tList = []
bList = []
cpuList = []
ramList = []
h1List = []
hddList = []
h2List = []
osList = []
yrList = []


with open ("C:\\Users\\andra\\Desktop\\Interm-Python\\lab2b-1.csv") as csvfile: #accesssing file and naming it
    file = csv.reader(csvfile)
    for row in file:
        counter += 1
        tList.append(row[0].upper())
        type = row[0]
        bList.append(row[1].upper())
        cpuList.append(row[2])
        ramList.append(row[3])
        h1List.append(row[4])
        hddList.append(row[5])
        if (row[5] == "2"):
            h2List.append(row[6])
            osList.append(row[7])
            yrList.append(row[8])
            yr = int(row[8])
        elif (row[5] == "1" ):
            h2List.append("N/A")
            osList.append(row[6])
            yrList.append(row[7])
            yr = int(row[7])

        if (yr < current-2):
            if (type == "D"):
                desktop += 1
            elif (type == "L"):
                laptop += 1

dcost = dcost * desktop
lcost = lcost * laptop

#TESTING
#for x in range (0, counter):
#    print(tList[x], " ", bList[x], " ", cpuList[x], " ", ramList[x], " ", h1List[x], " ", hddList[x], " ", h2List[x], " ", osList[x], " ", yrList[x])


print("To replace {0} Desktops it will cost ${1:7}".format(desktop, dcost))
print("To replace {0}  Laptops it will cost  ${1:7}".format(laptop, lcost))
 