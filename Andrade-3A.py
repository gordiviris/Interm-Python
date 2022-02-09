#Kevin Andrade
#SE126.02
#January 24, 2022
#Lab 3A

#Variable Dictionary

#file      holds all file info.
#type      stores if pc is a Desktop or Laptop
#brand     stores brand of PC
#cpu       stores cpu of PC
#ram       amount of ram in PC
#hdd1      amount of storage on 1st Disk
#numhdd    num of Disk in the system
#hdd2      amount of storage on 2nd Disk
#os        operating system on PC
#yr        year of the PC
#current   current year
#desktop   number of desktops to be replaced
#laptop    number of laptops to be replaced
#dcost     cost to replace desktops
#lcost     cost to replace laptops
#========== Main Code ==========

import csv

current = 22
desktop = 0
laptop = 0
lcost = 1500
dcost = 2000


with open ("C:\\Users\\andra\\Desktop\\Interm-Python\\lab2b-1.csv") as csvfile: #accesssing file and naming it
    file = csv.reader(csvfile)
    for row in file:
        type = row[0].upper()
        brand = row[1].upper()
        cpu = row[2]
        ram = row[3]
        hdd1 = row[4]
        numhdd = row[5]
        if numhdd == "2":
            hdd2 = row[6]
            os = row[7]
            yr = int(row[8])
        else:
            hdd2 = "    "
            os = row[6]
            yr = int(row[7])

        if (yr < current-2):
            if (type == "D"):
                desktop += 1
            elif (type == "L"):
                laptop += 1

dcost = dcost * desktop
lcost = lcost * laptop

print("To replace {0} Desktops it will cost ${1:8}".format(desktop, dcost))
print("To replace {0} Laptops it will cost ${1:8}".format(laptop, lcost))
 