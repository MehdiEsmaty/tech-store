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
- Docker
- Docker Compose

## نصب و راه‌اندازی

### روش 1: اجرا با Docker (توصیه شده)

1. کلون کردن مخزن:
```bash
git clone https://github.com/your-username/tech-store.git
cd tech-store
```

2. ساخت و اجرای کانتینر:
```bash
docker-compose up --build
```

3. دسترسی به برنامه:
```
http://localhost:8000
```

### روش 2: اجرا به صورت محلی

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
├── Dockerfile         # فایل پیکربندی Docker
├── docker-compose.yml # فایل پیکربندی Docker Compose
├── static/            # فایل‌های استاتیک
│   ├── css/
│   ├── js/
│   └── images/
└── templates/         # قالب‌های HTML
```

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. 