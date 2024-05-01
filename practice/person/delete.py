from dbutils.execute import execute_query

def delete_person(uid):
    query = f"delete from persons where uid = {uid};"

    execute_query(query)