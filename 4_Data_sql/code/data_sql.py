import psycopg2 # pip install psycopg2
import pandas as pd

# toad sql

connection = psycopg2.connect(
        user = "postgres",
        password = "postgres",
        host = "localhost", # 198.16.16.01, 127.0.0.1, www.prod.xxxcompany.com
        port = "5432",
        database = "week8"
    )

cursor = connection.cursor()
cursor.execute("SELECT * from employee;")
record = cursor.fetchall()
# cursor.commit() - must when 

# cursor.execute("Select * FROM mytable LIMIT 0")
colnames = [desc[0] for desc in cursor.description]

df = pd.DataFrame(record)
df.columns = colnames

df.to_csv(r'D:\Documents\python\repo\Introduction_Python\4_Data_sql\data\mysqldata.csv')

print("Printing database .............")

print(df)

print("Done!")

cursor.close()
connection.close()


cursor.execute("""CREATE TABLE myname (
    id integer NOT NULL PRIMARY KEY,
    firstname  text NOT NULL,
    lastname   text,
    citizenId  text,
    age        numeric
);""")

connection.commit()
cursor.close()
connection.close()

# INSERT INTO mytable
# (id,
# firstname,
# lastname)
# VALUES
# ('hi', 'Temuge',	'Erdene');

# INSERT INTO mytable
# (id,firstname,lastname,citizenid,age)
# VALUES (25, 'Khongorzul',	'Gantulga', 'UB95',22);

# #copy (SELECT * FROM employee
# where firstname LIKE 'B%')
#   TO 'D:\Documents\python\repo\Introduction_Python\4_Data_sql\data\exported.csv'
#   WITH DELIMITER ','
#   CSV HEADER
# ;

# sql
# psql manual
# psql in terminal
# psql in python
# 
# create table
#
#
