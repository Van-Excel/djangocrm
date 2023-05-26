import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Technicalking1.',

)

# prepare a cursor object
cursorObject = database.cursor()

# create A database
cursorObject.execute('CREATE DATABASE crm')

print('all done')
