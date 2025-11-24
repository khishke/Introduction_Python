
import psycopg2
import pandas as pd

# -----------------------------
# 1. PostgreSQL-т холбогдох
# -----------------------------
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="095009",
    port="5432"
)

# -----------------------------
# 2. Top 10 customers query
# -----------------------------
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

# pandas dataframe руу шууд унших
df_top_customers = pd.read_sql(top_customers_query, connection)

# -----------------------------
# 3. Dataframe-г үзүүлэх
# -----------------------------
print(df_top_customers)

# -----------------------------
# 4. Холболтыг хаах
# -----------------------------
connection.close()
