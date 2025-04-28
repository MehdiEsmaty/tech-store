from app import db, Product, Category

# Create tables
db.create_all()

# Add categories
categories = [
    Category(name="Mobile Phones", icon="bi-phone"),
    Category(name="Laptops", icon="bi-laptop"),
    Category(name="Tablets", icon="bi-tablet"),
    Category(name="Accessories", icon="bi-headphones"),
    Category(name="Smart Watches", icon="bi-watch")
]

for category in categories:
    db.session.add(category)

# Add sample products
products = [
    Product(
        name="iPhone 14 Pro",
        brand="Apple",
        price=999.99,
        discount_price=899.99,
        description="Latest iPhone with A16 Bionic chip",
        image="iphone14.jpg",
        category="Mobile Phones",
        stock=50
    ),
    Product(
        name="MacBook Pro M2",
        brand="Apple",
        price=1299.99,
        description="Powerful laptop with M2 chip",
        image="macbook.jpg",
        category="Laptops",
        stock=30
    ),
    Product(
        name="Galaxy S23",
        brand="Samsung",
        price=799.99,
        discount_price=749.99,
        description="Samsung's flagship smartphone",
        image="s23.jpg",
        category="Mobile Phones",
        stock=40
    )
]

for product in products:
    db.session.add(product)

# Commit changes
db.session.commit()
print("Database initialized with sample data!") 