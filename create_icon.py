from PIL import Image, ImageDraw, ImageFont

# Icon - Red eye with warning
img = Image.new('RGB', (512, 512), color='black')
draw = ImageDraw.Draw(img)

# Outer red glow
draw.ellipse([50, 50, 462, 462], fill='#330000', outline='red', width=15)

# Eye
draw.ellipse([100, 100, 412, 412], fill='#660000', outline='red', width=10)

# Pupil
draw.ellipse([200, 200, 312, 312], fill='black')

# Inner red dot
draw.ellipse([240, 240, 272, 272], fill='red')

img.save('icon.png')
print("✓ Icon created")

# Presplash - Warning screen
img2 = Image.new('RGB', (800, 1280), color='black')
draw2 = ImageDraw.Draw(img2)

# Warning border
draw2.rectangle([20, 20, 780, 1260], outline='red', width=5)

# Text
try:
    font_large = ImageFont.truetype("/system/fonts/DroidSans-Bold.ttf", 60)
    font_small = ImageFont.truetype("/system/fonts/DroidSans.ttf", 30)
except:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

draw2.text((400, 400), '⚠ BEYOND 9 ⚠', fill='red', anchor='mm', font=font_large)
draw2.text((400, 500), 'Reality Breach Protocol', fill='yellow', anchor='mm', font=font_small)
draw2.text((400, 800), 'WARNING:', fill='red', anchor='mm', font=font_small)
draw2.text((400, 850), 'May detect entities', fill='white', anchor='mm', font=font_small)
draw2.text((400, 900), 'invisible to human eye', fill='white', anchor='mm', font=font_small)

img2.save('presplash.png')
print("✓ Presplash created")
