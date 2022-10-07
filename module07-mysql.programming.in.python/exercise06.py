from mysql import connector

host = "localhost"
user = "root"
password = "Secret_123"
database = "world"
mysql_connection = connector.connect(host=host, user=user, password=password, database=database)

my_cursor = mysql_connection.cursor()

my_cursor.execute("""
    delete from employees
    where salary > 500000
""")
mysql_connection.commit()
print(f"{my_cursor.rowcount} row(s) deleted.")
