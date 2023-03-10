from PIL import Image, ImageFont, ImageDraw

save_path = "cert/"
font_file = ImageFont.truetype(r'LibreBaskerville-Italic.ttf', 60)
date_font = ImageFont.truetype(r'Muli-Regular.ttf', 50)
dept_file = ImageFont.truetype(r'Quicksand-Medium.ttf', 60)
font_colour = "#6d412a"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def generate_cert(name,college,event,dept,symp="Sample",date="10/03/2023"):
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width = draw.textlength(name, font = font_file)
    college_width = draw.textlength(college, font = font_file)
    event_width = draw.textlength(event, font = font_file)
    dept_width = draw.textlength(dept, font = dept_file)
    date_width = draw.textlength(date, font = date_font)
    symp_width = draw.textlength(symp, font = font_file)

    draw.text(((WIDTH - name_width) / 1.45, (HEIGHT - 755)), name, fill = font_colour, font = font_file)
    draw.text(((WIDTH - college_width) / 1.9, (HEIGHT - 655)), college, fill = font_colour, font = font_file)
    draw.text(((WIDTH - event_width) / 1.85, (HEIGHT - 555)), event, fill = font_colour, font = font_file)
    draw.text(((WIDTH - symp_width) / 3.4, (HEIGHT - 453)), symp, fill = font_colour, font = font_file)
    draw.text(((WIDTH - date_width) / 1.29, (HEIGHT - 432)), date, fill = "#000000", font = date_font)
    draw.text(((WIDTH - dept_width) / 2, (HEIGHT - 1150)), dept, fill = "#343434", font = dept_file)
    return image_source