import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Lampard_180489',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE user")

print('All Done!')