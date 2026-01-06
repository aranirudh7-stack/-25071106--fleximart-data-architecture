# FlexiMart Database Schema Documentation

## Overview
This document describes the relational database schema designed for the FlexiMart transactional system. The schema follows normalization principles to reduce redundancy and maintain data integrity.

---

## Tables Description

### 1. Customers
Stores customer profile information.

**Attributes:**
- customer_id (Primary Key)
- first_name
- last_name
- email
- phone
- city
- registration_date

---

### 2. Products
Stores product catalog details.

**Attributes:**
- product_id (Primary Key)
- product_name
- category
- price
- stock_quantity

---

### 3. Orders
Represents customer orders.

**Attributes:**
- order_id (Primary Key)
- customer_id (Foreign Key → Customers)
- order_date
- total_amount
- status

---

### 4. Order_Items
Stores individual items within an order.

**Attributes:**
- order_item_id (Primary Key)
- order_id (Foreign Key → Orders)
- product_id (Foreign Key → Products)
- quantity
- unit_price
- subtotal

---
## Normalization Explanation (3NF)

The FlexiMart database is designed in Third Normal Form (3NF) to eliminate redundancy and ensure data integrity.

In the customers table, the primary key (customer_id) uniquely determines first_name, last_name, email, phone, city, and registration_date. There are no partial dependencies, and all attributes depend only on the primary key.

In the products table, product_id uniquely identifies product_name, category, price, and stock_quantity. Category information is stored once per product, avoiding repetition across transactions.

The orders table separates order-level data such as order_date and total_amount from item-level data, preventing update anomalies. Each order references exactly one customer via a foreign key.

The order_items table resolves the many-to-many relationship between orders and products. Each non-key attribute (quantity, unit_price, subtotal) depends entirely on the composite relationship.

This design avoids:
- **Update anomalies**: Product price updates occur in one place
- **Insert anomalies**: Orders can exist without items initially
- **Delete anomalies**: Deleting an order does not remove customer data
---

## Relationships
- One customer can place many orders
- One order can contain multiple products
- Each product can appear in multiple orders
