use fleximart_nosql;

// Load data
db.products.insertMany([
  {
    product_id: "ELEC001",
    name: "Samsung Galaxy S21",
    category: "Electronics",
    price: 79999,
    stock: 150,
    reviews: [{user:"U001",rating:5,comment:"Great",date:new Date("2024-01-15")}]
  }
]);

// Query 1
db.products.find(
  {category:"Electronics", price:{$lt:50000}},
  {name:1,price:1,stock:1,_id:0}
);

// Query 2
db.products.aggregate([
  {$unwind:"$reviews"},
  {$group:{_id:"$name",avg_rating:{$avg:"$reviews.rating"}}},
  {$match:{avg_rating:{$gte:4}}}
]);

// Update
db.products.updateOne(
  {product_id:"ELEC001"},
  {$push:{reviews:{user:"U999",rating:4,comment:"Good value",date:new Date()}}}
);

// Aggregation
db.products.aggregate([
  {$group:{_id:"$category",avg_price:{$avg:"$price"},product_count:{$sum:1}}},
  {$sort:{avg_price:-1}}
]);
