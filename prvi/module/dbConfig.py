import mysql.connector

def dbConnect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "aaa"
    )