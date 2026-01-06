# Star Schema Design – FlexiMart Data Warehouse

## Overview
The FlexiMart data warehouse is designed using a **star schema** to support fast analytical queries and reporting.

The schema consists of:
- One **fact table** (sales_fact)
- Multiple **dimension tables**

---

## Fact Table

### Sales_Fact
Stores transactional sales metrics.

**Measures:**
- quantity_sold
- total_sales_amount

**Foreign Keys:**
- customer_id
- product_id
- date_id

---

## Dimension Tables

### Dim_Customer
- customer_id (PK)
- customer_name
- city
- registration_date

### Dim_Product
- product_id (PK)
- product_name
- category
- price

### Dim_Date
- date_id (PK)
- full_date
- month
- quarter
- year

---

## Benefits of Star Schema
- Simple design
- Faster query performance
- Optimized for OLAP queries
