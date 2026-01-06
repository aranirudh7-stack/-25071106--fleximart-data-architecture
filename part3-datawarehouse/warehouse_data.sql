-- Sample Dimension Data

INSERT INTO dim_customer VALUES
('C001','Rahul Sharma','Bangalore','2023-01-15'),
('C002','Priya Patel','Mumbai','2023-02-20');

INSERT INTO dim_product VALUES
('P001','Samsung Galaxy S21','Electronics',45999),
('P002','Nike Running Shoes','Fashion',3499);

INSERT INTO dim_date VALUES
(20240115,'2024-01-15',1,1,2024),
(20240116,'2024-01-16',1,1,2024);

-- Sample Fact Data

INSERT INTO sales_fact 
(customer_id, product_id, date_id, quantity_sold, total_sales_amount)
VALUES
('C001','P001',20240115,1,45999),
('C002','P002',20240116,2,6998);
