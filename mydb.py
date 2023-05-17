import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", passwd="2105")


# prepare a cursor object
cursor_object = dataBase.cursor()

# create a database
cursor_object.execute("CREATE DATABASE `django-crm`;")

print("All Done")
