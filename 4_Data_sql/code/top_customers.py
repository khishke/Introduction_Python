# GitHub-д upload test

import psycopg2
import pandas as pd

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="095009",
    port="5432"
)

top_customers_query = """
SELECT 
    c.customer_id,
    c.fullname,
    COUNT(i.invoice_id) AS total_orders,
    SUM(ii.line_total) AS total_spent
FROM customers c
JOIN invoices i ON c.customer_id = i.customer_id
JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
GROUP BY c.customer_id, c.fullname
ORDER BY total_spent DESC
LIMIT 10;
"""

df_top_customers = pd.read_sql(top_customers_query, connection)

print(df_top_customers)

connection.close()
