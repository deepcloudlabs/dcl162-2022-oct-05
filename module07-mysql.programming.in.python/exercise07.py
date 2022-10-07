from mysql import connector

host = "localhost"
user = "root"
password = "Secret_123"
database = "world"
mysql_connection = connector.connect(host=host, user=user, password=password, database=database)

my_cursor = mysql_connection.cursor()

my_cursor.execute("""
    set session transaction isolation level read uncommitted
    set session transaction isolation level read committed
    set session transaction isolation level repeatable read
    set session transaction isolation level serializable
""")
mysql_connection.commit()
print(f"{my_cursor.rowcount} row(s) deleted.")
