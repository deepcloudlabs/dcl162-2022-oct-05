from mysql import connector

host = "localhost"
user = "root"
password = "Secret_123"
database = "world"
mysql_connection = connector.connect(host=host, user=user, password=password, database=database)

my_cursor = mysql_connection.cursor()

my_cursor.execute("""
    create table employees(
        identity char(11) primary key,
        fullname varchar(128) not null,
        salary float,
        iban char(28)
    ) engine=innodb
""")

"""
mysql> show tables;
+-----------------+
| Tables_in_world |
+-----------------+
| city            |
| country         |
| countrylanguage |
| employees       |
+-----------------+
4 rows in set (0.00 sec)
mysql> desc employees;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| identity | char(11)     | NO   | PRI | NULL    |       |
| fullname | varchar(128) | NO   |     | NULL    |       |
| salary   | float        | YES  |     | NULL    |       |
| iban     | char(28)     | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
4 rows in set (0.00 sec)
"""