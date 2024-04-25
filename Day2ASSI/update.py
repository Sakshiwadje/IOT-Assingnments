

import mysql.connector


def get_connection():
    conn= mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb"
    )
    return conn

def update_person(empid, salary):
    
    conn = get_connection()

    query = f"update employee SET salary = %s where empid = %s;"
    val = (salary, empid)

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()



update_person(2, 40000)

