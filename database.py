import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bala@2471password",
    database="imagecon"
    )
mycursor=mydb.cursor()
# mycursor.execute("create database employeedatabasemanagement")
# print("databse created successfully")

mycursor.execute("create table employees_details(Employee_Id varchar(250),Name varchar(250),Age int,DOJ varchar(200),Email varchar(200),Gender varchar(200),Contact_No varchar(100),Position varchar(200))")
print("table created successfully")


