# فروشگاه آنلاین فناوری

یک فروشگاه آنلاین ساده با استفاده از Flask و SQLAlchemy

## ویژگی‌ها

- نمایش محصولات
- دسته‌بندی محصولات
- سبد خرید
- پرداخت آنلاین
- مدیریت موجودی

## نیازمندی‌ها

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Pillow

## نصب و راه‌اندازی

1. کلون کردن مخزن:
```bash
git clone https://github.com/your-username/tech-store.git
cd tech-store
```

2. نصب نیازمندی‌ها:
```bash
pip install -r requirements.txt
```

3. راه‌اندازی دیتابیس:
```bash
python init_db.py
```

4. اجرای برنامه:
```bash
python app.py
```

## ساختار پروژه

```
tech-store/
├── app.py              # فایل اصلی برنامه
├── init_db.py          # اسکریپت راه‌اندازی دیتابیس
├── create_images.py    # اسکریپت ایجاد تصاویر نمونه
├── requirements.txt    # فایل نیازمندی‌ها
├── static/            # فایل‌های استاتیک
│   ├── css/
│   ├── js/
│   └── images/
└── templates/         # قالب‌های HTML
```

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. 