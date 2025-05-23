from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

# Database Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount_price = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.String(100))
    category = db.Column(db.String(50))
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50))

# Routes
@app.route('/')
def index():
    categories = Category.query.all()
    featured_products = Product.query.filter_by(category='featured').limit(8).all()
    new_products = Product.query.order_by(Product.created_at.desc()).limit(8).all()
    return render_template('index.html', 
                         categories=categories,
                         featured_products=featured_products,
                         new_products=new_products)

@app.route('/category/<category_name>')
def category(category_name):
    products = Product.query.filter_by(category=category_name).all()
    return render_template('category.html', products=products, category=category_name)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.contains(query)).all()
    return render_template('search_results.html', products=products, query=query)

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    total_price = 0
    tax = 0
    
    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        if product:
            total_price += product.price * quantity
    
    tax = total_price * 0.09  # 9% tax
    
    return render_template('cart.html', total_price=total_price, tax=tax, Product=Product)

@app.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    product = Product.query.get_or_404(product_id)
    
    if quantity > product.stock:
        flash('موجودی کافی نیست.', 'error')
        return redirect(url_for('cart'))
    
    cart = session.get('cart', {})
    cart[str(product_id)] = quantity
    session['cart'] = cart
    
    flash('سبد خرید بروزرسانی شد.', 'success')
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    
    flash('محصول از سبد خرید حذف شد.', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    if not session.get('cart'):
        flash('سبد خرید شما خالی است.', 'error')
        return redirect(url_for('index'))
    
    cart = session.get('cart', {})
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        if product:
            total_price += product.price * quantity
    
    tax = total_price * 0.09  # 9% tax
    
    return render_template('checkout.html', total_price=total_price, tax=tax)

@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    # Here you would typically:
    # 1. Validate the form data
    # 2. Process the payment
    # 3. Create an order record
    # 4. Clear the cart
    # 5. Send confirmation email
    
    flash('سفارش شما با موفقیت ثبت شد. به زودی با شما تماس خواهیم گرفت.', 'success')
    session['cart'] = {}
    return redirect(url_for('index'))

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        quantity = int(request.form.get('quantity', 1))
        
        if quantity > product.stock:
            flash('موجودی کافی نیست.', 'error')
            return redirect(url_for('product_detail', product_id=product_id))
        
        cart = session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
        session['cart'] = cart
        
        flash(f'{quantity} عدد {product.name} به سبد خرید اضافه شد.', 'success')
        return redirect(url_for('cart'))
    except Exception as e:
        flash('خطایی در اضافه کردن محصول به سبد خرید رخ داد.', 'error')
        return redirect(url_for('product_detail', product_id=product_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000) 