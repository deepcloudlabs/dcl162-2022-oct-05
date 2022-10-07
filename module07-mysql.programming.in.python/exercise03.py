from mysql import connector

host = "localhost"
user = "root"
password = "Secret_123"
database = "world"
mysql_connection = connector.connect(host=host, user=user, password=password, database=database)

my_cursor = mysql_connection.cursor()

my_cursor.execute("""
    insert into employees values
    ("1", "jack bauer", 100000, "tr1"),
    ("2", "kate austen", 200000, "tr2"),
    ("3", "james sawyer", 300000, "tr3"),
    ("4", "sun kwon", 400000, "tr4")
""")
mysql_connection.commit()
print(f"{my_cursor.rowcount} row(s) inserted.")
