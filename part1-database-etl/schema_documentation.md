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

## Normalization
The database schema is designed in **Third Normal Form (3NF)**:
- Each table represents a single entity
- No partial dependencies
- No transitive dependencies

---

## Relationships
- One customer can place many orders
- One order can contain multiple products
- Each product can appear in multiple orders
