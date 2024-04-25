

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
