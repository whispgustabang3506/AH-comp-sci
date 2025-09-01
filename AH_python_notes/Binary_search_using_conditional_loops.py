#Binary search using conditional loops

numbers = [0,6,7,9,16,25,26,34,40,48,57,59,67,72,79,82,80,91,100,101,105,112,118,123,129,134,141,147,152,166,173,180]

target = 173
startpos = 0
endpos = len(numbers)-1
counter = 0
found = False

while found == False and (startpos<=endpos):
    middle = int((startpos+endpos)//2)
    if numbers[middle] == target:
        found = True
    elif numbers[middle] < target:
        startpos = middle + 1
    else:
        endpos = middle - 1
    counter += 1

if found == True: 
    print("The target", target, "was found in", counter, "iterations")

if found == False:
    print("We were unable to find the target,", target, " in the array")

