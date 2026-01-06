# FlexiMart Data Architecture Project


## Project Overview
End-to-end data architecture project for an e-commerce platform, covering ETL pipelines, SQL analytics, MongoDB operations, and data warehouse modeling using a star schema.

**Student Name:** R Anirudh  
**Student Code:** bitsom_ba_25071106  
**Email:** aranirudh7@gmail.com  
**Date:** 04-Jan-2026  

---

## Project Overview

The FlexiMart Data Architecture Project focuses on designing and implementing a complete data ecosystem for a retail business. The project includes building an ETL pipeline to extract, transform, and load transactional data into a relational database, performing NoSQL operations for product catalog management using MongoDB, and creating a star schema–based data warehouse for advanced analytics.

The project demonstrates integration of structured and semi-structured data, efficient query handling, and analytical reporting to support business decision-making.

---

## Repository Structure
             
├── part1-database-etl/             
│   ├── etl_pipeline.py         
│   ├── schema_documentation.md               
│   ├── business_queries.sql          
│   └── data_quality_report.txt             
├── part2-nosql/                         
│   ├── nosql_analysis.md           
│   ├── mongodb_operations.js                 
│   └── products_catalog.js                                     
├── part3-datawarehouse/                                          
│   ├── star_schema_design.md                         
│   ├── warehouse_schema.sql                      
│   ├── warehouse_data.sql                                  
│   └── analytics_queries.sql                                
└── README.md                 

                     
---

## Technologies Used

- Python 3.x, pandas, mysql-connector-python  
- MySQL 8+  
- MongoDB 6.0  

---
## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

- Built an end-to-end data architecture integrating relational databases, NoSQL systems, and data warehouses.
- Implemented ETL pipelines using Python and SQL for reliable data transformation and loading.
- Gained hands-on experience with MongoDB CRUD operations and aggregation pipelines.
- Designed a star schema to support analytical queries and reporting.

---

## Challenges Faced

- Handling data quality issues during ETL such as missing values and duplicates.
- Managing MongoDB connections and aggregation queries.
- Designing an optimized star schema for analytical workloads.
