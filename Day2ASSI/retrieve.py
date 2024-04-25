
import mysql.connector
  conn = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        databse = "iotdb"

    )  
    return conn

query = "select * from employee;"

cursor = connection.cursor()

cursor.execute(query)

records = cursor.fetchall()

print(records)

cursor.close()

connection.close()
