# Based on this example: https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
# python Pillow_example.py image.jpg "Text to add"

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import sys

img = Image.open(sys.argv[1])
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("consola.ttf", 32)

# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((10, 10), sys.argv[2], (255,255,255), font=font)
img.save('output.jpg')