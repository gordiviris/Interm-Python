#kevin andrade
#demo week 7
#february 23, 2022

def swap(list,j):
    temp = list[j]
    list[j] = list[j+1]
    list[j+1] = temp



names = ["Sam","Carole","Adam","Bill"]

for x in range(0,4):
    for y in range(0,3):
        if (names[y] > names[y+1]):
            swap(names, y)
            #temp = names[y]
            #names[y] = names[y+1]
            #names[y+1]= temp

print (names)