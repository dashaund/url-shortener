import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testuser",
  password="CHANGEME",
  database="testdb",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

sql_select_Query = "select * from urls"
mycursor.execute(sql_select_Query)
records = mycursor.fetchall()
print("Total number of rows in urls is: ", mycursor.rowcount)

print("Key        URL\n_______________\n")
for row in records:
        print(row[0]+"      "+row[1]+"\n")

# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)

if (mydb.is_connected()):
        mydb.close()
        mycursor.close()
        print("MySQL connection is closed")