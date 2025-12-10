from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create the database engine
engine = create_engine("sqlite:///shop.db", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    user = relationship("User", back_populates="orders")
    product = relationship("Product")


Base.metadata.create_all(engine)


user1 = User(name= "Bob Smith", email="bsmith@email.com")
user2 = User(name= "Robert Smith", email="rsmith@email.com")

product1 = Product(name="Laptop", price=1200)
product2 = Product(name="Headphones", price=150)
product3 = Product(name="Coffee Mug", price=20)

order1 = Order(user=user1, product=product1, quantity=1)
order2 = Order(user=user1, product=product3, quantity=2)
order3 = Order(user=user2, product=product2, quantity=1)
order4 = Order(user=user2, product=product3, quantity=3)


session.add_all([user1, user2, product1, product2, product3, order1, order2, order3, order4])
session.commit()

print("\n-- All Users ---")
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

print("\n--- All Products ---")
products = session.query(Product).all()
for product in products:
    print(f"Name: {product.name}, Price: ${product.price}")

# 3️⃣ Retrieve all orders showing user's name, product name, and quantity
print("\n--- All Orders ---")
orders = session.query(Order).all()
for order in orders:
    print(f"User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")

# 4️⃣ Update a product's price (example: update 'Laptop' to 1000)
print("\n--- Updating Product Price ---")
laptop = session.query(Product).filter_by(name="Laptop").first()
if laptop:
    laptop.price = 1000
    session.commit()
    print(f"Updated {laptop.name} price to ${laptop.price}")

# 5️⃣ Delete a user by ID (example: delete user with id = 1)
print("\n--- Deleting User with ID = 1 ---")
user_to_delete = session.query(User).filter_by(id=1).first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"Deleted user: {user_to_delete.name}")

# Confirm remaining users
print("\n--- Remaining Users ---")
for user in session.query(User).all():
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
