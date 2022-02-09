#Kevin Andrade
#SE126.02
#January 11, 2022
#Lab 1A

#Variable dictionary
#key    key to enter while loop
#cap    room max capacity
#att    people wanting to attend
#dif    difference between cap and att


#----------Main Code----------
print("Capacity Checker")

key = "y"

#MAIN WHILE LOOP
while(key=="y"):
    
    cap = int(input("What is the capacity of the room? "))
    att = int(input("How many people want to attend the event? "))
    dif = cap - att
    
    if (dif<0):
        dif = abs(dif)
        print("{0} people have to be told they cannot attend the meeting".format(dif))
    else:
        print("The Conference can be held. {0} more people can attend.".format(dif))
    key = input("Do you want to check anymore rooms (y/n)?").lower()




