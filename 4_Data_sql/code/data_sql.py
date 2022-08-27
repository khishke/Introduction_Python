import psycopg2
import pandas as pd

# toad sql

connection = psycopg2.connect(
        user = "postgres",
        password = "postgres",
        host = "localhost",
        port = "5432",
        database = "mydata"
    )

cursor = connection.cursor()
cursor.execute("SELECT * from mytable;")
record = cursor.fetchall()

# cursor.execute("Select * FROM mytable LIMIT 0")
colnames = [desc[0] for desc in cursor.description]

df = pd.DataFrame(record)
df.columns = colnames

df.to_csv('mysqldata.csv')

cursor.close()
connection.close()


# CREATE TABLE mytable (

#     id integer NOT NULL PRIMARY KEY,
#     firstname      text NOT NULL,
#     lastname   text NOT NULL
# );

# INSERT INTO mytable
# (id,
# firstname,
# lastname)
# VALUES
# ('hi', 'Temuge',	'Erdene');

# INSERT INTO mytable
# (id,
# firstname,
# lastname)
# VALUES
# (2, 'Khongorzul',	'Gantulga');


