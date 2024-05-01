from dbutils.execute import execute_query


def update_person(choice, nvalue, uid):
    if choice == 'address':
        query = f"update persons SET address='{nvalue}' where uid = {uid};"
    elif choice == 'mobile':
        query = f"update persons SET mobile='{nvalue}' where uid = {uid};"

    execute_query(query)