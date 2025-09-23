#host doesnt change since we are running it locally 
#type pip install mysql-connector-python in the terminal if you get an error message 

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

c.execute("""SELECT * FROM client""")

for row in c:
  print('Client ID', row[0])
  print('Name', row[1])
  print('Address', row[2])
  print('PhoneNo', row[3])
  print('FaxNo', row[4])
c.close()