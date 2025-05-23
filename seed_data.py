from app import db, Product, Category
from datetime import datetime

def seed_database():
    # Create categories
    categories = [
        Category(name='موبایل', icon='bi-phone'),
        Category(name='لپ تاپ', icon='bi-laptop'),
        Category(name='تبلت', icon='bi-tablet'),
        Category(name='لوازم جانبی', icon='bi-headphones'),
        Category(name='featured', icon='bi-star')  # Special category for featured products
    ]
    
    for category in categories:
        db.session.add(category)
    
    # Create products
    products = [
        Product(
            name='گوشی موبایل سامسونگ گلکسی S23',
            brand='Samsung',
            price=25000000,
            discount_price=23000000,
            description='گوشی هوشمند سامسونگ با پردازنده قدرتمند و دوربین پیشرفته',
            image='samsung-s23.jpg',
            category='موبایل',
            stock=10
        ),
        Product(
            name='لپ تاپ اپل مک بوک پرو',
            brand='Apple',
            price=45000000,
            discount_price=43000000,
            description='لپ تاپ اپل با پردازنده M2 و نمایشگر رتینا',
            image='macbook-pro.jpg',
            category='لپ تاپ',
            stock=5
        ),
        Product(
            name='تبلت اپل آیپد پرو',
            brand='Apple',
            price=30000000,
            description='تبلت اپل با قابلیت های پیشرفته و قلم دیجیتال',
            image='ipad-pro.jpg',
            category='تبلت',
            stock=8
        ),
        Product(
            name='هدفون بی سیم سونی WH-1000XM4',
            brand='Sony',
            price=15000000,
            discount_price=14000000,
            description='هدفون بی سیم با نویز کنسلینگ پیشرفته',
            image='sony-headphones.jpg',
            category='لوازم جانبی',
            stock=15
        ),
        Product(
            name='گوشی موبایل آیفون 14 پرو',
            brand='Apple',
            price=35000000,
            description='گوشی هوشمند اپل با دوربین 48 مگاپیکسلی',
            image='iphone-14-pro.jpg',
            category='featured',
            stock=7
        )
    ]
    
    for product in products:
        db.session.add(product)
    
    # Commit all changes
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database() 