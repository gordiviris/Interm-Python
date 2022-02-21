#Kevin Andrade
#SE126.02
#February 14, 2022
#Lab 5A

#Variable Dictionary
#ipList     List that holds all ip addresses in a file
#length     length of ipList
#ipAddy     holds one value from ipList to pass through to ipClass() function

#---------- Functions ----------
def ipClass(num):
    '''Takes in an IP address and determinies if it is a class B address and prints it out with its subnet mask'''
    slist = num.split(".")
    firstInt = int(slist[0])

    if(firstInt >= 128 and firstInt <= 191):
        subnet = "255.255.0.0"
        print("{0:20} {1}".format(num,subnet))


#========== Main Code ==========
import csv
print("Class B IP's         Subnet Masks\n---------------------------------")

ipList = []
with open("Lab5a.csv") as csvfile: #Importing file and saving ips into a list
    file = csv.reader(csvfile)
    for row in file:
        ipList.append(row[0])
        

length = len(ipList)    #getting length of the list
for x in range (0,length):  #for loop that sends each ip throight ipClass function
    ipAddy = ipList[x]
    ipClass(ipAddy)


