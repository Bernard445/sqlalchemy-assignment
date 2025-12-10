# 🐍 SQLAlchemy Relational Database Project

### 📘 Objective
This project demonstrates how to create and manage a relational database using **Python** and **SQLAlchemy ORM**.  
It defines three tables — `User`, `Product`, and `Order` — sets up relationships between them, and performs basic **CRUD** (Create, Read, Update, Delete) operations.

---

## 🧱 Part 1: Setup

**Technologies Used**
- Python 3.x  
- SQLAlchemy  
- SQLite (for simplicity)

### Installation
1. Install SQLAlchemy:
   ```bash
   pip install SQLAlchemy
🧩 Part 2: Tables and Relationships

Tables Created:

User

id (Primary Key)

name (String)

email (Unique String)

Relationship: One user can have many orders.

Product

id (Primary Key)

name (String)

price (Integer)

Order

id (Primary Key)

user_id (Foreign Key → User.id)

product_id (Foreign Key → Product.id)

quantity (Integer)

Relationships:

Belongs to one User

Belongs to one Product

🏗️ Part 3: Table Creation

All tables are created automatically using:

Base.metadata.create_all(engine)

📦 Part 4: Inserted Sample Data
👤 Users
Name	Email
Bob Smith	bsmith@email.com

Robert Smith	rsmith@email.com
🛒 Products
Name	Price
Laptop	1200
Headphones	150
Coffee Mug	20
📦 Orders
User	Product	Quantity
Bob Smith	Laptop	1
Bob Smith	Coffee Mug	2
Robert Smith	Headphones	1
Robert Smith	Coffee Mug	3
🔍 Part 5: Queries Performed

Retrieve all users and print their information.

Retrieve all products and print their name and price.

Retrieve all orders, showing each user’s name, product name, and quantity.

Update a product’s price (e.g., update “Laptop” price from 1200 → 1000).

Delete a user by ID.

Each query is demonstrated with output in the console when you run the script.
