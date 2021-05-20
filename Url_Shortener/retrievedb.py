import mysql.connector

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


# rankey = "TNqt5"
# url = retrieve(rankey)
#
# print(url)