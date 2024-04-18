
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_employee(empid, dept):
    
    conn = get_connection()

    query = f"update employees SET dept = %s where empid = %s;"
    val = (dept, empid)

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    cursor.close()
    conn.close()


update_employee(24, "E3")












