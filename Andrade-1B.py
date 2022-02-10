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

key = "y" #key set up to enter loop first time

#MAIN WHILE LOOP
while(key=="y"):
    
    cap = int(input("\nWhat is the capacity of the room? "))
    att = int(input("How many people want to attend the event? "))
    dif = cap - att
    

    if (dif<0):
        dif = abs(dif) #set dif to its absolute val. in case of neg. num
        print("\n{0} people have to be told they cannot attend the meeting".format(dif))
    else:
        print("\nThe Conference can be held. {0} more people can attend.".format(dif))
    key = input("\nDo you want to check anymore rooms (y/n)? ").lower() #.lower() changes user input to lowercase  
    
    while(key != "y" and key != "n"): #Enters while loop when anything other than "y" or "n" is entered
      print("\n**ERROR** Invalid Entry!")
      key = input("Do you want t0 check anymore rooms? (y/n) ").lower()

    
