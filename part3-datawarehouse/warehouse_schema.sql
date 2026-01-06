-- Dimension Tables

CREATE TABLE dim_customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    registration_date DATE
);

CREATE TABLE dim_product (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    month INT,
    quarter INT,
    year INT
);

-- Fact Table

CREATE TABLE sales_fact (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    date_id INT,
    quantity_sold INT,
    total_sales_amount DECIMAL(12,2),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
