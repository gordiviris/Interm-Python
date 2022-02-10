#Kevin Andrade
#SE126.02
#January 11, 2022
#Lab 1A

#Variable dictionary
#key    key to enter while loop
#cap    room max capacity
#att    people wanting to attend
#dif    difference between cap and att

from os import system, name
#----------Functions----------
def clear(): 
  
  # for windows 
  if name == 'nt': 
    _ = system('cls') 

  else: 
    _ = system('clear') 


def capacity():
  limit = int(input("\nWhat is the capacity of this room? "))
  return limit

def attendees():
  attend = int(input("How many people want to attend the event? "))
  return attend

def register(max, numP):
  result = max - numP
  return result

def roomCheck():
  answer = input("\nDo you want to check anymore rooms (y/n)? ").lower() #.lower() changes user input to lowercase  
    
  while(answer != "y" and answer != "n"): #Enters while loop when anything other than "y" or "n" is entered
      print("\n**ERROR** Invalid Entry!")
      answer = input("Do you want t0 check anymore rooms? (y/n) ").lower()
  return answer


#----------Main Code----------
print("Capacity Checker")

key = "y" #key set up to enter loop first time

#MAIN WHILE LOOP
while(key=="y"):
    
    cap = capacity()
    att = attendees()
    dif = register(cap, att)
    

    if (dif<0):
        dif = abs(dif) #set dif to its absolute val. in case of neg. num
        print("\n{0} people have to be told they cannot attend the meeting".format(dif))
    else:
        print("\nThe Conference can be held. {0} more people can attend.".format(dif))
    key = roomCheck()
clear()
print("Thank you for using Capacity Checker!")