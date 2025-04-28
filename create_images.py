from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(text, filename, size=(400, 300)):
    # Create a new image with a light gray background
    image = Image.new('RGB', size, color=(240, 240, 240))
    draw = ImageDraw.Draw(image)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=(100, 100, 100), font=font)
    
    # Save image
    image.save(filename)

# Create directory if it doesn't exist
os.makedirs('static/images/products', exist_ok=True)

# Create placeholder images
create_placeholder_image('Hero Image', 'static/images/hero-image.jpg')
create_placeholder_image('iPhone 14', 'static/images/products/iphone14.jpg')
create_placeholder_image('MacBook Pro', 'static/images/products/macbook.jpg')
create_placeholder_image('Galaxy S23', 'static/images/products/s23.jpg')

print("Placeholder images created successfully!") 