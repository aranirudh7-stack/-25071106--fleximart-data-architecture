-- Total sales by product
SELECT 
    p.product_name,
    SUM(f.total_sales_amount) AS total_sales
FROM sales_fact f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name;

-- Sales by city
SELECT 
    c.city,
    SUM(f.total_sales_amount) AS city_sales
FROM sales_fact f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.city;

-- Monthly sales trend
SELECT 
    d.year,
    d.month,
    SUM(f.total_sales_amount) AS monthly_sales
FROM sales_fact f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
