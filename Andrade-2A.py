#Kevin Andrade
#SE126.02
#January 19, 2022
#Lab 2A

#Variable dictionary

#recCount     counter for receords processed
#over         counter for rooms over limit
#room         stores room name from file
#limit        stores max capacity from file
#att          stores num of attendees from file
#check        subtracts att from limit to check over cap.

#==========Main Code==========
import csv

recCount = 0
over = 0

print("Room\t\t\t   Max\t     Min       Over")

with open("C:\\Users\\andra\\OneDrive\\Desktop\\PYTHON SE126\\lab2a.csv") as csvfile:
  file = csv.reader(csvfile)
  for row in file:
    recCount += 1
    room = row[0]
    limit = int(row[1])
    att = int(row[2])
    check = limit - att
    if (check < 0):
      check = abs(check)
      over += 1
      print("{0:20}{1:10}{2:10}{3:10}".format(room, limit, att, check))
    
print("\nProcessed ", recCount, " records")
print("There are ", over, " rooms over the limit")