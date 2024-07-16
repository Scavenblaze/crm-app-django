import mysql.connector

#interacts with mysql server
Database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysqlpassword123'
)


#prepare cursor object
#cursor is used to execute sql commands
cursorObject = Database.cursor()

#create database
cursorObject.execute("CREATE DATABASE crm_db")

print("Done!")