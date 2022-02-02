from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files import File

def water_mark(image):
    im = Image.open(image)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "this is test"

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    margin = 500
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x,y), text, font=font)
    im.show()
    thumb_io = BytesIO()
    im.save(thumb_io, 'PNG', quality=50)
    thumbnail = File(thumb_io, name=image.name)

    return thumbnail
