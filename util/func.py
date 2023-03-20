from PIL import Image, ImageFont, ImageDraw

save_path = "cert/"
font_file = ImageFont.truetype(r'util\LibreBaskerville-Italic.ttf', 60)
date_font = ImageFont.truetype(r'util\Muli-Regular.ttf', 50)
dept_file = ImageFont.truetype(r'util\Quicksand-Medium.ttf', 60)
hod_file = ImageFont.truetype(r'util\Fraunces_9pt_SuperSoft-Light.ttf', 40)
font_colour = "#6d412a"

template = Image.open(r'util\template.png')
WIDTH, HEIGHT = template.size


def generate_cert(name,college,event,dept,symp,date,conv):
    dept = "Department of "+dept
    image_source = Image.open(r'util\template.png')
    draw = ImageDraw.Draw(image_source)
    name_width = draw.textlength(name, font = font_file)
    college_width = draw.textlength(college, font = font_file)
    event_width = draw.textlength(event, font = font_file)
    dept_width = draw.textlength(dept, font = dept_file)
    date_width = draw.textlength(date, font = date_font)
    symp_width = draw.textlength(symp, font = font_file)
    conv_width = draw.textlength(conv, font = hod_file)
    
    if dept=="Department of Computer Science and Engineering":
        hod_sign = Image.open(r'util\sign\CSE.png').resize((600, 600), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Electronics and Communication Engineering":
        hod_sign = Image.open(r'util\sign\ECE.png').resize((500, 500), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Electrical and Electronics Engineering":
        hod_sign = Image.open(r'util\sign\EEE.png').resize((650, 650), Image.ANTIALIAS)
        image_source.paste(hod_sign, (330, 850), hod_sign)
    elif dept=="Department of Mechanical Engineering":
        hod_sign = Image.open(r'util\sign\MECH.png').resize((550, 550), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Civil Engineering":
        hod_sign = Image.open(r'util\sign\CIVIL.png').resize((600, 580), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Computer Science and Business Systems":
        hod_sign = Image.open(r'util\sign\CSBS.png').resize((600, 600), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900))
    elif dept=="Department of Artificial Intelligence and Data Science":
        hod_sign = Image.open(r'util\sign\AIDS.png').resize((600, 600), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Computer and Communication Engineering":
        hod_sign = Image.open(r'util\sign\CCE.png').resize((600, 600), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)
    elif dept=="Department of Information Technology":
        hod_sign = Image.open(r'util\sign\IT.png').resize((600, 600), Image.ANTIALIAS)
        image_source.paste(hod_sign, (380, 900), hod_sign)

    draw.text(((WIDTH - name_width) / 1.45, (HEIGHT - 755)), name, fill = font_colour, font = font_file)
    draw.text(((WIDTH - college_width) / 1.9, (HEIGHT - 655)), college, fill = font_colour, font = font_file)
    draw.text(((WIDTH - event_width) / 1.85, (HEIGHT - 555)), event, fill = font_colour, font = font_file)
    draw.text(((WIDTH - symp_width) / 3.4, (HEIGHT - 453)), symp, fill = font_colour, font = font_file)
    draw.text(((WIDTH - date_width) / 1.29, (HEIGHT - 432)), date, fill = "#000000", font = date_font)
    draw.text(((WIDTH - dept_width) / 2, (HEIGHT - 1150)), dept, fill = "#343434", font = dept_file)
    draw.text(((WIDTH - conv_width) / 3.5, (HEIGHT - 175)), conv, fill ="#000000" , font = hod_file)
    return image_source