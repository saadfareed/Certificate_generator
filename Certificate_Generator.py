import pandas as pd
from PIL import Image, ImageDraw, ImageFont
#process
data = pd.read_csv (r'Git and Git-Hub.csv') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'Untitled-1.jpg')
    d = ImageDraw.Draw(im)
    fon = ImageFont.truetype("arial.ttf", 60)
    location = (700, 650)
    text_color = (0, 46, 99)
    d.text(location, i, fill = text_color,font=fon ,stroke_width=2)
    im.save("certificate_" + i + ".pdf")
