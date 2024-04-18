# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# form a qery
query = "select * from employees;"
query1 = "select dept from employees;"
query2 = "select * from employees order by salary DESC;"


cursor = connection.cursor()

cursor.execute(query)

records = cursor.fetchall()    

print(records)

cursor = connection.cursor()

cursor.execute(query1)

records = cursor.fetchall()    

print(records)

cursor = connection.cursor()

cursor.execute(query2)

records = cursor.fetchall()    

print(records)

cursor.close()

connection.close()