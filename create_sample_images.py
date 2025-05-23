from PIL import Image, ImageDraw
import os
from random import randint

def create_gradient(size, start_color, end_color):
    width, height = size
    image = Image.new('RGB', size)
    pixels = image.load()
    
    for y in range(height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * y / height)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * y / height)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * y / height)
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    return image

def create_product_image(name, brand, size=(800, 800)):
    # Create a gradient background
    if brand == 'Apple':
        bg = create_gradient(size, (220, 220, 220), (200, 200, 200))
    elif brand == 'Samsung':
        bg = create_gradient(size, (200, 220, 255), (180, 200, 235))
    elif brand == 'Sony':
        bg = create_gradient(size, (0, 0, 0), (40, 40, 40))
    else:
        bg = create_gradient(size, (240, 240, 240), (220, 220, 220))
    
    draw = ImageDraw.Draw(bg)
    
    # Add decorative elements based on product type
    center_x = size[0] // 2
    center_y = size[1] // 2
    
    if 'موبایل' in name:
        # Phone shape
        draw.rounded_rectangle([(center_x-60, center_y-120), (center_x+60, center_y+120)], 
                             radius=20, fill=(50, 50, 50))
        draw.rectangle([(center_x-50, center_y-110), (center_x+50, center_y+110)], 
                      fill=(200, 200, 200))
    elif 'لپ تاپ' in name:
        # Laptop shape
        draw.rounded_rectangle([(center_x-150, center_y-80), (center_x+150, center_y+80)], 
                             radius=10, fill=(50, 50, 50))
        draw.rounded_rectangle([(center_x-140, center_y-70), (center_x+140, center_y+70)], 
                             radius=5, fill=(200, 200, 200))
    elif 'تبلت' in name:
        # Tablet shape
        draw.rounded_rectangle([(center_x-100, center_y-130), (center_x+100, center_y+130)], 
                             radius=20, fill=(50, 50, 50))
        draw.rounded_rectangle([(center_x-90, center_y-120), (center_x+90, center_y+120)], 
                             radius=15, fill=(200, 200, 200))
    else:
        # Headphones shape
        draw.ellipse([(center_x-80, center_y-80), (center_x+80, center_y+80)], 
                    fill=(50, 50, 50))
        draw.ellipse([(center_x-70, center_y-70), (center_x+70, center_y+70)], 
                    fill=(200, 200, 200))
    
    return bg

def create_hero_image(size=(1200, 600)):
    # Create a gradient background
    bg = create_gradient(size, (0, 123, 255), (0, 80, 200))
    draw = ImageDraw.Draw(bg)
    
    # Add decorative elements
    for i in range(0, size[0], 50):
        opacity = randint(30, 70)
        draw.line([(i, 0), (i+100, size[1])], fill=(255, 255, 255, opacity), width=2)
    
    # Add circles
    for _ in range(5):
        x = randint(0, size[0])
        y = randint(0, size[1])
        radius = randint(20, 100)
        opacity = randint(30, 70)
        draw.ellipse([(x-radius, y-radius), (x+radius, y+radius)], 
                    outline=(255, 255, 255, opacity), width=3)
    
    return bg

def main():
    # Create directories if they don't exist
    os.makedirs('static/images/products', exist_ok=True)
    os.makedirs('static/images/hero', exist_ok=True)
    
    # Create product images
    products = [
        ('samsung-s23.jpg', 'گوشی موبایل سامسونگ گلکسی S23', 'Samsung'),
        ('macbook-pro.jpg', 'لپ تاپ اپل مک بوک پرو', 'Apple'),
        ('ipad-pro.jpg', 'تبلت اپل آیپد پرو', 'Apple'),
        ('sony-headphones.jpg', 'هدفون بی سیم سونی WH-1000XM4', 'Sony'),
        ('iphone-14-pro.jpg', 'گوشی موبایل آیفون 14 پرو', 'Apple')
    ]
    
    for filename, name, brand in products:
        img = create_product_image(name, brand)
        img.save(f'static/images/products/{filename}', quality=95)
        print(f'Created {filename}')
    
    # Create hero image
    hero_img = create_hero_image()
    hero_img.save('static/images/hero/tech-hero.jpg', quality=95)
    print('Created tech-hero.jpg')

if __name__ == '__main__':
    main() 