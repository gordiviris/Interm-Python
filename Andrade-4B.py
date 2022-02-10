#Kevin Andrade
#SE126.02
#February 2, 2022
#Lab 4B

#Variable Dictionary

#key      key to enter main while loop
#rowA     holds all "A" seats
#rowB     holds all "B" seats
#rowC     holds all "C" seats
#rowD     holds all "D" seats
#taken    holds "true" or "false" to check if seat is taken or not
#row      number of row desired
#letter   letter of seat desired

#==========FUNCTIONS==========

def chart(a,b,c,d):
    '''Display seatiing chart!'''

    for x in range(1,8):
        print(" ",x," ",a[x]," ",b[x],"   ",c[x]," ",d[x])

def seat():
    '''asks user for number row wanted'''
    row= int(input("\nEnter row desired (1-7): "))
    return row

def let():
    '''asks user for letter of seat wanted'''
    abcd= input("Enter seat desired (A, B, C, or D): ").upper()
    return abcd

def again():
    '''asks ueer if they want to enter another seat'''
    answer = input("Would you like to select another seat? [Y/N] ").upper()
    while answer != "Y" and answer != "N":
        print("**ERROR** Invalid Input")
        answer = input("Would you like to select another seat? [Y/N] ").upper()
    if(answer == "N"):
        print("Thank you for using MySeat Selection! Goodbye :]")

    return answer

#========== Main Code ==========
print("    MySeat Selection\n")

#LIST of all seats
rowA = ["","A","A","A","A","A","A","A"]
rowB = ["","B","B","B","B","B","B","B"]
rowC = ["","C","C","C","C","C","C","C"]
rowD = ["","D","D","D","D","D","D","D"]

#initializing key and taken value
taken="false"
key="Y"

chart(rowA, rowB, rowC, rowD) #Display seat chart

while(key=="Y"): #MAIN LOOP STARTS
    row = seat() #NUMBER OF ROW
    letter = let() #LETTER OF SEAT
    #print(row,letter)

    #if and elif statements change taken to true or false and if false, it replaces the letter with an X 
    if (letter == "A"):
        if (rowA[row] == "X"):
            taken = "true"
        else:
            taken = "false"
            rowA[row]="X"

    elif(letter == "B"):
        if (rowB[row] == "X"):
            taken = "true"
        else:
            taken = "false"
            rowB[row] = "X"

    elif(letter == "C"):
        if (rowC[row] == "X"):
            taken = "true"
        else:
            taken = "false"
            rowC[row] = "X"

    elif(letter == "D"):
        if (rowD[row] == "X"):
            taken = "true"
        else:
            taken = "false"
            rowD[row] = "X"
    else:
        print("**ERROR** Invalid Input") #Error statement if user enters unwanted value

    if (taken == "true"): #dsiplays taken message if seat is taken already
        print("\nSorry! This seat is already taken!") 
    else: #dsiplays seat chosen if it was available
        print("\nYou have choosen Seat {0}{1}!\n".format(row,letter))
    
    chart(rowA, rowB, rowC, rowD) #displaying chart again

    key = again() #user input to see if they want to enter another seat