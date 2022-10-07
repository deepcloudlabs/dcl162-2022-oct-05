from mysql import connector

host = "localhost"
user = "root"
password = "Secret_123"
database = "world"
mysql_connection = connector.connect(host=host, user=user, password=password, database=database)

my_cursor = mysql_connection.cursor()

my_cursor.execute("""
    select identity, fullname, salary, iban
    from employees
    limit 0,10
""")
for row in my_cursor.fetchall():
    print(f"{row[1]} {row[2]}")
