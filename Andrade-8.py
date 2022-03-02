#Kevin Andrade
#SE126.02
#February 28, 2022
#Lab 8


#========== FUNCTIONS ==========
def chart(num,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    
    print("     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4\n")
    print("1  ",end=" ")
    for x in range (0,num):
        print(a[x],end = " ")
    print("")
    print("2  ",end=" ")    
    for x in range (0,num):
        print(b[x],end = " ")
    print("")  
    print("3  ",end=" ")
    for x in range (0,num):
        print(c[x],end = " ")
    print("")
    print("4  ",end=" ")
    for x in range (0,num):
        print(d[x],end = " ")
    print("")
    print("5  ",end=" ")
    for x in range (0,num):
        print(e[x],end = " ")
    print("")
    print("6  ",end=" ")
    for x in range (0,num):
        print(f[x],end = " ")
    print("")
    print("7  ",end=" ")
    for x in range (0,num):
        print(g[x],end = " ")
    print("")
    print("8  ",end=" ")
    for x in range (0,num):
        print(h[x],end = " ")
    print("")
    print("9  ",end=" ")
    for x in range (0,num):
        print(i[x],end = " ")
    print("")
    print("10 ",end=" ")
    for x in range (0,num):
        print(j[x],end = " ")
    print("")
    print("11 ",end=" ")
    for x in range (0,num):
        print(k[x],end = " ")
    print("")
    print("12 ",end=" ")
    for x in range (0,num):
        print(l[x],end = " ")
    print("")
    print("13 ",end=" ")
    for x in range (0,num):
        print(m[x],end = " ")
    print("")
    print("14 ",end=" ")
    for x in range (0,num):
        print(n[x],end = " ")
    print("")
    print("15 ",end=" ")
    for x in range (0,num):
        print(o[x],end = " ")
    print()



def numrow(a):
    num = int(input("Enter desired row number:  "))
    while num > a or num < 1:
        print("*ERROR* Invalid Selection")
        num = int(input("Enter desired row number:  "))

    return num



def numcol():
    num = input("Enter desired seat letter: ")
    return num



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



def update(rownum,colnum,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    if rownum == 1:
        if a[colnum] == "*":
            taken = "true"
        else:
            taken = "false"
            a[colnum] = "*"

    

    

    return taken




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

chart(seats,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15)
print("")
numtix = amount()
totalprice= 0
for x in range (0,numtix):
    y = x+1
    print("Ticket #{}".format(y))
    inrow = numrow(rows)
    incol = numcol()
    price = tixprice(inrow)
    totalprice = totalprice + price
    update(inrow,incol,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15)

print("total {0}".format(totalprice))
    

