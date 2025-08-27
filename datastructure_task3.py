
# Instructions  

  ## Challenge
  #1. Modify the code so that the program asks the user for their initials and for a row and column on the bus
  #2. It then checks to see if the row and column are free
  #3. If it is free the initials are added to that 2D array location
  #4. If it is not free an error message is displayed and the user asked for another row and column 

# Bus example
rownum = 6 # total number of rows available 
colnum = 7 #total number of collums available

seat = [["" for x in range(colnum)] for y in range(rownum)] # "" means void  untaken seats are void 
seat[0][0] = 'D'

seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'

seat[1][2] = 'T'

initial = input("what are your intials?")
chosen_row = int(input("please enter choose your row")) 
chosen_collum = int(input("please enter and choose your collum"))  

while seat[chosen_row][chosen_collum] != "": #if the seat is not void (taken)
  print("yo the seat is lowk taken")
  chosen_row = int(input("please enter choose your row")) 
  chosen_collum = int(input("please enter your chosen collum"))
  

if seat[chosen_row][chosen_collum] == "":
  seat[chosen_row][chosen_collum] = 1
  print("your booking is sucessful")

for x in range(rownum):
  row = ""
  for y in range(colnum):
    row += str(seat[x][y])+ ","

row = row[:-1]
print(row)


