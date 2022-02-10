#Kevin Andrade
#SE126.02
#February 2, 2022
#Lab 4C

#Variable Dictionary

#frst     List of firt names
#last     list of last names
#pNum     list of phone numbers
#mail     list of emails
#dept     list of departments
#posi     list of positions
#found    true or false if last name was found in registry (last[])
#length   Length of Last[]
#num      stores the index of where the name was found
#search   user entered last name  

#========== Main Code ==========
import csv

#initializing lists and found key
frst = []
last = []
pNum = []
mail = []
dept = []
posi = []
found = "false"
#importing csv file
with open("C:\\Users\\andra\\OneDrive\\Desktop\\PYTHON SE126\\lab4c.csv") as csvfile:
    lab4c = csv.reader(csvfile)
    #appending all info to appropiate lists
    for row in lab4c:
        frst.append(row[0])
        last.append(row[1])
        pNum.append(row[2])
        mail.append(row[3])
        dept.append(row[4])
        posi.append(row[5])

length = len(last) #length of list for "for" loop
print("\tEmployee Registry\nNumber of Employees: ",length) #prints number of employees in the csv file
search = input("Enter last name of employee: ") #user enters last name of employee they are looking for

for x in range(0, length):    #for loop to try and find user entered last name
    if last[x] == search:     #if the last name is found then found is true and index is stored 
        num = x
        found = "true"
if (found == "true"): #prints employees infprmation if they were found 
    print("\n\tInformation\nName:     {0} {1}\nPhone#:   {2}\nEmail:    {3}\nDept:     {4}\nPosition: {5}".format(frst[num],last[num],pNum[num],mail[num],dept[num],posi[num]))
else:
    print("Employee not found!")

