import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testuser",
  password="CHANGEME",
  database="testdb",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE urls (rankey VARCHAR(5) NOT NULL PRIMARY KEY, url VARCHAR(255) NOT NULL)")

if (mydb.is_connected()):
        mydb.close()
        mycursor.close()
        print("MySQL connection is closed")