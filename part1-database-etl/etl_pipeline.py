import pandas as pd
import mysql.connector
import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "fleximart"
}

DATA_PATH = "../data/"

def format_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r'\D', '', str(phone))
    return f"+91-{digits[-10:]}" if len(digits) >= 10 else None

def format_date(date_val):
    try:
        return pd.to_datetime(date_val).strftime('%Y-%m-%d')
    except:
        return None

def standardize_category(cat):
    return cat.strip().title() if pd.notna(cat) else "Unknown"

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

report = []

# ---------------- CUSTOMERS ----------------
customers = pd.read_csv(DATA_PATH + "customers_raw.csv")
orig = len(customers)

customers.drop_duplicates(inplace=True)
customers["email"].fillna("unknown@example.com", inplace=True)
customers["phone"] = customers["phone"].apply(format_phone)
customers["registration_date"] = customers["registration_date"].apply(format_date)

for _, row in customers.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO customers
        (first_name,last_name,email,phone,city,registration_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

report.append(f"Customers Processed: {orig}")
report.append(f"Customers Loaded: {len(customers)}")

# ---------------- PRODUCTS ----------------
products = pd.read_csv(DATA_PATH + "products_raw.csv")
orig = len(products)

products.drop_duplicates(inplace=True)
products["price"].fillna(products["price"].mean(), inplace=True)
products["stock_quantity"].fillna(0, inplace=True)
products["category"] = products["category"].apply(standardize_category)

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products
        (product_name,category,price,stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, tuple(row))

report.append(f"Products Processed: {orig}")
report.append(f"Products Loaded: {len(products)}")

# ---------------- SALES ----------------
sales = pd.read_csv(DATA_PATH + "sales_raw.csv")
orig = len(sales)

sales.drop_duplicates(inplace=True)
sales.dropna(subset=["customer_id","product_id"], inplace=True)
sales["transaction_date"] = sales["transaction_date"].apply(format_date)

for _, row in sales.iterrows():
    cursor.execute("""
        INSERT INTO orders (customer_id,order_date,total_amount,status)
        VALUES (%s,%s,%s,%s)
    """, (
        row["customer_id"],
        row["transaction_date"],
        row["quantity"] * row["unit_price"],
        row["status"]
    ))

report.append(f"Sales Processed: {orig}")
report.append(f"Sales Loaded: {len(sales)}")

conn.commit()

with open("data_quality_report.txt","w") as f:
    f.write("\n".join(report))

cursor.close()
conn.close()
