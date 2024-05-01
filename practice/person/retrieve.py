from dbutils.execute import execute_select_query

def get_persons():
    query = "select * from persons;"

    return execute_select_query