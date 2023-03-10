from PIL import Image, ImageFont, ImageDraw

save_path = "cert/"
font_file = ImageFont.truetype(r'util\AlexBrush-Regular.ttf', 120)
font_colour = "#6d412a"

template = Image.open(r'util\template.png')
WIDTH, HEIGHT = template.size

def generate_cert(name,college,event,dept):
    image_source = Image.open(r'util\template.png')
    draw = ImageDraw.Draw(image_source)
    name_width = draw.textlength(name, font = font_file)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - 835)), name, fill = font_colour, font = font_file)
    return image_source