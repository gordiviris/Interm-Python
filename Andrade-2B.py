#Kevin Andrade
#SE126.02
#January 20, 2022
#Lab 2B

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

#========== Main Code ==========

import csv

print("Type\t\tBrand\t  CPU  RAM    1st Disk  No HDD\t 2nd Disk     OS  YR")
with open ("C:\\Users\\andra\\OneDrive\\Desktop\\PYTHON SE126\\lab2b-1.csv") as csvfile:
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
            yr = row[8]
        else:
            hdd2 = "    "
            os = row[6]
            yr = row[7]


        if type == "D": #IF statement to determine what type of PC it is
            type = "Desktop"
        elif type == "L":
            type = "Laptop"

        if brand == "DL": #IF statement to determine brand of pc
            brand = "Dell"
        elif brand == "GW":
            brand = "Gateway"

        print("{0}\t\t{1}\t  {2}\t{3}\t{4}\t   {5}\t  {6}\t     {7}  {8}".format(type, brand, cpu, ram, hdd1, numhdd, hdd2, os, yr))

        