from pymongo import MongoClient

def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.fleximart_nosql
    collection = db.products

    # Insert sample documents
    collection.insert_many([
        {"product_id": "P006", "name": "Organic Honey", "category": "Groceries", "price": 450},
        {"product_id": "P007", "name": "HP Laptop", "category": "Electronics", "price": 52999}
    ])

    # Find all products
    for product in collection.find():
        print(product)

    # Aggregation: count products per category
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}}
    ]
    result = collection.aggregate(pipeline)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
