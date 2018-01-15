from PIL import Image, ImageFont, ImageDraw

img = Image.open("img.jpg", "r")

width, height = img.size

font = ImageFont.truetype("lobster.ttf", 100)

draw = ImageDraw.Draw(img)

text_x, text_y =font.getsize("Cool Parks")
x = (width - text_x)/2
y = (height - text_y)/2

draw.text((x, y), "Cool Parks", (255, 255, 255), font=font)

img.save("formatted.jpg")
