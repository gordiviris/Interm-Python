#Kevin Andrade
#SE126.02
#February 23, 2022
#Lab 7

#========== Functions ==========

def swap(list,num):
    '''function swaps values of 2 variables or list element'''
    temp = list[num]
    list[num] = list[num+1]
    list[num+1] = temp

def highSort(list1,list2,list3,list4,list5):
    '''sorts a list from highest to lowest'''
    length = len(list1)
    for y in range (0,length):
        for x in range (0, length-1):
            if (list1[x] < list1[x+1]):
                swap(list2,x)
                swap(list3,x)
                swap(list4,x)
                swap(list5,x)
                swap(list1,x)

def mySort(list1, list2, list3, list4, list5):
    '''sorts a list from lowest to highest'''
    num = len(list1)
    for y in range (0,num):
        for x in range (0, num-1):
            if (list1[x] > list1[x+1]):
                swap(list1,x)
                swap(list2,x)
                swap(list3,x)
                swap(list4,x)
                swap(list5,x)


def raise5(list1):
    '''calculates a 5 percent increase from a list of numbers'''
    num = len(list1)
    total = 0
    for x in range(0,num):
        total= (list1[x] * 0.05) + total
    return total

def avgSlry(list1, list2):
    '''finds average salary of a specific department'''
    length= len(list1)
    totalSlry = 0
    misCount = 0
    for x in range(0,length):
        if(list2[x] == "MIS"):
            misCount += 1
            totalSlry = totalSlry + list1[x]
    avg = totalSlry / misCount
    return avg

#========== Variable Dictionary ==========
#frst       list of all first names
#last       list of all last names
#dept       list of everyones department
#epos       list of everyones position
#slry       list of employees salary
#temp       temporary list to hold cancatenated lists
#average    average salary
#cost       cost of rasing salaries by 5 percent
#length     length of the list
    

#========== Main Code ==========
import csv
#initializing lists
frst = []
last = []
dept = []
epos = []
slry = []
temp = []
#importing file and placing it into designated lists
with open("Lab7.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for row in file:
        frst.append(row[0])
        last.append(row[1])
        dept.append(row[2])
        epos.append(row[3])
        slry.append(int(row[4]))



print("TOP 10 HIGHEST SALARIES")
print("==================================")
highSort(slry,frst,last,dept,epos) #sending slry list first to be sorted by highest nnumber
for x in range(0,10): #printing list
    print("{0:10}{1:15}${2:8,}".format(last[x],dept[x],slry[x]))



print("\n\nAVERAGE SALARY FOR MIS DEPT.")
print("==================================")
average = avgSlry(slry, dept) #sending slry and dept to find the avg salary of MIS employees
print("${0:,.2f}".format(average)) #printing average number



print("\n\nTOP 10 LOWEST SALARIES")
print("==================================")
mySort(slry,frst,last,epos,dept) #sending slry first to sort the lists based on lowest salary first
for x in range(0,10): #for loop to print each row 
    print("{0:10}{1:10}{2:8}${3:8,}".format(frst[x],last[x],dept[x],slry[x]))
    


print("\n\nCOST OF 5% RAISE TO ALL EMPLOYEES")
print("==================================")
cost = raise5(slry) #sending slry of all workers
print("${0:,.2f}".format(cost)) #printing resu;t




print("\n\nDEPTARTMENTS IN ALPHABETICAL ORDER")
print("      FIRST & LAST 5 RECORDS")
print("==================================")
length = len(dept)
for x in range(0,length):
    temp.append(dept[x]+last[x]) #cancatenating two lists together into a temp list

mySort(temp,dept,frst,last,slry) #sending temp list first to sort based on the cancatenated list

for x in range(0,5):#printing first 5 records
    #print("{0} {1}".format(last[x],dept[x]))
    print("{0:8} {1:8} {2:14} ${3:8,}".format(last[x],frst[x],dept[x],slry[x]))
for x in range(length-5,length): #printing last 5 records
    print("{0:8} {1:8} {2:8} ${3:8,}".format(last[x],frst[x],dept[x],slry[x]))







