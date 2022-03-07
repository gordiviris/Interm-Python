#Kevin Andrade
#SE126.02
#March 7, 2022
#Lab 9

#========== Functions ==========
def swap(list,num):
    '''function swaps values of 2 variables or list element'''
    temp = list[num] 
    list[num] = list[num+1] 
    list[num+1] = temp 

def mySort(list1,list2):
    '''sorts a list from lowest to highest'''
    num = len(list1)
    for y in range (0,num):
        for x in range (0, num-1):
            if (list1[x] > list1[x+1]):
                swap(list1,x)
                swap(list2,x)

#========== Variable Dictionary ==========
#frst      list of all first names
#last      list of all last names
#length    length of a list


#========== Main Code ==========
import csv
frst = []
last = []

with open("Lab9.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        frst.append(row[0])
        last.append(row[1])
csvfile.close()

mySort(last,frst)

with open ("E:\Python126\Lab9BWrite.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(frst)
    writer.writerow(last)
csvfile.close()

#length = len(frst)
#for x in range(0,length):
#    print(last[x],frst[x])

