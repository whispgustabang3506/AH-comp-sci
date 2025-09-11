#irving micheal innes 
#suits
suitrank = ["hearts", "spades", "diamonds", "clubs"]
mycards = ['1 hearts', '13 spades', '1 clubs', '10 diamonds', '5 spades', '5 hearts']

def bubblesort(mylist, sootrank):
    for outer in range (len(mylist)-1,0,-1):
        for inner in range(outer):
            if int(mylist[inner].split()[0]) > int(mylist[inner+1]).split()[0]):   #aplit gets rid of the gap 

        