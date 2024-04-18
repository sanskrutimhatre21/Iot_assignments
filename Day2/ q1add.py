import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

empid = int(input("Entere empid : "))
name = input("Enter name : ")
dept = input("Enter dept :")
email = input("Enter email :")
salary = int(input("Enter salary : "))
doj = input("Enter date of joining :")

query = f"insert into employees values({empid}, '{name}', '{dept}', '{email}', '{salary}', '{doj}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
 
connection.close()