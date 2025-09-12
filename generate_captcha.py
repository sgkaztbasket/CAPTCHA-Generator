import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def random_text(length=6):
    """Generate a random string of uppercase letters and digits."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def distort_text(draw, text, font, width, height):
    """Draw the text with random position and rotation for each character."""
    spacing = width // len(text)
    for i, char in enumerate(text):
        angle = random.randint(-30, 30)
        y = random.randint(0, height - font.size)
        char_img = Image.new('RGBA', (spacing, height), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, y), char, font=font, fill=(0, 0, 0))
        char_img = char_img.rotate(angle, resample=Image.BICUBIC, expand=1)
        draw.bitmap((i * spacing, 0), char_img, fill=None)

def add_noise(draw, width, height):
    """Add random noise (lines and dots) to the image."""
    for _ in range(6):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=(0, 0, 0), width=1)
    for _ in range(30):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(0, 0, 0))

def generate_captcha(filename="captcha.png", length=6):
    width, height = 200, 70
    text = random_text(length)
    image = Image.new('RGB', (width, height), (255, 255, 255))
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except OSError:
        # fallback to default PIL font if arial.ttf is not found
        font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    add_noise(draw, width, height)
    distort_text(draw, text, font, width, height)
    add_noise(draw, width, height)

    image = image.filter(ImageFilter.GaussianBlur(1))

    image.save(filename)
    print(f"CAPTCHA text: {text}")
    print(f"Saved to {filename}")

if __name__ == "__main__":
    generate_captcha()
