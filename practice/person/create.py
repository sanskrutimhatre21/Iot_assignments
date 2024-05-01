from dbutils.execute import execute_query

def insert_person(uid, name, age, address, mobile):
    query = f"insert into persons values{uid}, '{name}', '{age}', '{address}', '{mobile}');"

    execute_query(query)