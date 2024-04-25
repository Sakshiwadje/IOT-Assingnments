
import mysql.connector
def get_connection():
    conn = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb"
)
return conn
empid = int(input("Enter empid :"))
name = input("Enter name :")
department = input("Enter department :")
email = input("Enter email :")
salary = int(input("Enter salary:"))
DOJ = input("Enter DOJ")

query = f"inser into employee values({empid}, '{name}', '{department}','{email}', {salary}, '{DOJ}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()
