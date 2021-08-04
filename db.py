import mysql.connector

def insert(rankey, url):
    mydb = mysql.connector.connect(
        host="localhost",
        user="testuser",
        password="CHANGEME",
        database="testdb",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO urls (rankey, url) VALUES (%s, %s)"
        val = (rankey, url)
        mycursor.execute(sql, val)
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
    except:
        sql = "UPDATE urls SET url = %s WHERE rankey = %s"
        val = (url, rankey)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Row has been updated")

    if (mydb.is_connected()):
        mydb.close()
        mycursor.close()
        print("MySQL connection is closed")

def retrieve(rankey):
    mydb = mysql.connector.connect(
        host="localhost",
        user="testuser",
        password="CHANGEME",
        database="testdb",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    val = (rankey)
    sql = "SELECT * FROM urls WHERE rankey='%s'" % val
    mycursor.execute(sql, val)
    records=mycursor.fetchall()

    for row in records:
        return row[1]