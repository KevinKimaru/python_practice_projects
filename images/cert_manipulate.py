from PIL import ImageDraw, ImageFont, Image

img = Image.open("cert.jpg", "r")
font = ImageFont.truetype("lobster.ttf", 30)
draw = ImageDraw.Draw(img)

width, height = img.size
text_x, text_y =font.getsize("Kevin Kimaru")
x = (width - text_x) / 2

draw.text((x, 174), "Kevin Kimaru", (33, 102, 56), font=font)
draw.text((x, 270), "Computer Science", (33, 102, 56), font=font)

img.save("formattedCert.png")
