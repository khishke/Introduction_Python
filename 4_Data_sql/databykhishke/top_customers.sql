CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    fullname VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(100),
    registered_date DATE
);

CREATE TABLE products (
    product_id      INT PRIMARY KEY,
    product_name    VARCHAR(200),
    category        VARCHAR(100),
    unit_price      NUMERIC(12,2),
    stock_qty       INT
);


CREATE TABLE invoices (
    invoice_id      INT PRIMARY KEY,
    customer_id     INT REFERENCES customers(customer_id),
    invoice_date    DATE,
    status          VARCHAR(20)
);

CREATE TABLE invoice_items (
    item_id     INT PRIMARY KEY,
    invoice_id  INT REFERENCES invoices(invoice_id),
    product_id  INT REFERENCES products(product_id),
    quantity    INT,
    line_total  NUMERIC(12,2)
);

CREATE TABLE payments (
    payment_id      INT PRIMARY KEY,
    invoice_id      INT REFERENCES invoices(invoice_id),
    amount          NUMERIC(12,2),
    payment_date    DATE,
    method          VARCHAR(20)
);

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM invoices;
SELECT COUNT(*) FROM invoice_items;
SELECT COUNT(*) FROM payments;

SELECT * FROM customers LIMIT 5;
SELECT * FROM invoices LIMIT 5;
SELECT * FROM invoice_items LIMIT 5;
SELECT * FROM payments LIMIT 5;
SELECT * FROM products LIMIT 5;

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

SELECT 
    p.category,
    SUM(ii.line_total) AS total_sales
FROM products p
JOIN invoice_items ii ON p.product_id = ii.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

SELECT 
    p.product_name,
    SUM(ii.quantity) AS qty_sold
FROM products p
JOIN invoice_items ii ON p.product_id = ii.product_id
GROUP BY p.product_name
ORDER BY qty_sold DESC
LIMIT 5;

SELECT 
    SUM(ii.line_total) AS pending_amount
FROM invoices i
JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
WHERE i.status = 'PENDING';

SELECT 
    DATE_TRUNC('month', i.invoice_date) AS month,
    SUM(ii.line_total) AS total_sales
FROM invoices i
JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
GROUP BY month
ORDER BY month;

SELECT 
    c.customer_id,
    c.fullname,
    COUNT(i.invoice_id) AS orders_count,
    MAX(i.invoice_date) AS last_order_date,
    SUM(ii.line_total) AS total_spent
FROM customers c
JOIN invoices i ON c.customer_id = i.customer_id
JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
GROUP BY c.customer_id, c.fullname
ORDER BY total_spent DESC
LIMIT 10;


