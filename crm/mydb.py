import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'joe',
    passwd = 'EXG04*Q&eB8o*jLb'
)

# Prepar a cursor object
cursorObject = dataBase.cursor()

# Create a DB
cursorObject.execute("CREATE DATABASE crm")

print("All done!")