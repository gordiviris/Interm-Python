#Kevin Andrade
#SE126.02
#February 28, 2022
#Lab 8


#========== FUNCTIONS ==========
def chart(num,a,b,c):
    print("         A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4\n")
    for i in range (0,5):
        print("row {0:2}".format(i+1),end="  ")
        for j in range (0,num):
            print(a[i][j],end=" ")
        print()
    

    for i in range (0,5):
        print("row {0:2}".format(i+6),end="  ")
        for j in range (0,num):
            print(b[i][j],end=" ")
        print()

    for i in range (0,5):
        print("row {0:2}".format(i+11),end="  ")
        for j in range (0,num):
            print(c[i][j],end=" ")
        print()
    

def numrow():
    num = int(input("Enter desired row number:  "))
    while num > 15 or num < 1:
        print("*ERROR* Invalid Selection")
        num = int(input("Enter desired row number:  "))

    return num



def numcol():
    num = input("Enter desired seat letter: ").lower()
    if (num == "1" or num == "2" or num == "3" or num == "4"):
        new = ord(num) - 22
    else:
        new = ord(num) - 96
    return new



def amount():
    num = int(input("How Many Tickets would you like to purchase?: "))
    return num



def tixprice(num):
    if num > 0 and num <= 5:
        money = 200
    elif num > 5 and num <= 10:
        money = 175
    elif num > 10 and num <= 15:
        money = 150

    return money



def update(num,rownum,colnum,a,b,c):

    avail = "false"
    while avail == "false":
        
        if(rownum > 0 and rownum <= 5):
            if a[rownum-1][colnum] == "*":
                avail = "false"
                print("\nSeat is already taken, please make another seleection!")
                rownum = numrow()
                colnum = numcol()
            else:
                avail = "true"
                a[rownum-1][colnum] = "*"

        elif(rownum >= 6 and rownum <= 10):
            if b[rownum-6][colnum] == "*":
                avail = "false"
                print("\nSeat is already taken, please make another seleection!")
                rownum = numrow()
                colnum = numcol()
            else:
                avail = "true"
                b[rownum-6][colnum] = "*"

        elif(rownum >= 11 and rownum <= 15):
            if c[rownum-11][colnum] == "*":
                avail = "false"
                print("\nSeat is already taken, please make another seleection!")
                rownum = numrow()
                colnum = numcol()
            else:
                avail = "true"
                c[rownum-11][colnum] = "*"

    key = input("Would you like to see available seats? [Y/N]: ").lower()
    
    while key == "y":
        counter = 0
        
        print("         A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4\n")
        for i in range (0,5):
            print("row {0:2}".format(i+1),end="  ")
            countRow = 0
            for j in range (0,num):
                print(a[i][j],end=" ")
                if a[i][j] == "*":
                    countRow += 1 
                    counter +=1
            print("....{} seats Available".format(30-countRow))
        

        for i in range (0,5):
            print("row {0:2}".format(i+6),end="  ")
            countRow = 0
            for j in range (0,num):
                print(b[i][j],end=" ")
                if b[i][j] == "*":
                    countRow += 1 
                    counter += 1
            print("....{} seats Available".format(30-countRow))

        for i in range (0,5):
            print("row {0:2}".format(i+11),end="  ")
            countRow = 0
            for j in range (0,num):
                print(c[i][j],end=" ")
                if c[i][j] == "*":
                    countRow += 1 
                    counter += 1
            print("....{} seats Available".format(30-countRow))

        print("\nThere are {} total seats available!".format(450-counter))

        key = "n"


#========== Main Code ==========

row1 = [""]
row2 = [""]
row3 = [""]
row4 = [""]
row5 = [""]
row6 = [""]
row7 = [""]
row8 = [""]
row9 = [""]
row10 = [""]
row11 = [""]
row12 = [""]
row13 = [""]
row14 = [""]
row15 = [""]


rows = 15
seats = 31
for x in range (0,seats):
    row1.append("#")
    row2.append("#")
    row3.append("#")
    row4.append("#")
    row5.append("#")
    row6.append("#")
    row7.append("#")
    row8.append("#")
    row9.append("#")
    row10.append("#")
    row11.append("#")
    row12.append("#")
    row13.append("#")
    row14.append("#")
    row15.append("#")

sec1 = [row1,row2,row3,row4,row5]
sec2 = [row6,row7,row8,row9,row10]
sec3 = [row11,row12,row13,row14,row15]
#print(sec1)
#print(sec2)
#print(sec3)

chart(seats,sec1,sec2,sec3)
print("")
numtix = amount()
totalprice= 0
for x in range (0,numtix):
    y = x+1
    print("\nTicket #{}".format(y))
    inrow = numrow()
    incol = numcol()
    #print(inrow)
    #print(incol)
    price = tixprice(inrow)
    totalprice = totalprice + price
    check = "y"
    while check == "y":
        check = input("Would you like to see your current total? [Y/N] ").lower()
        if check == "y":
            print("\nYour total is ${0:.2f}".format(totalprice))
            check = "n"
    update(seats,inrow,incol,sec1,sec2,sec3)
    

print("\nYour Grandtotal is ${0:.2f}".format(totalprice))