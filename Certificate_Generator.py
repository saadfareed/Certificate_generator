import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
#process
if os.path.exists('certificates'):
    print("Loading....")
else:
    os.mkdir('certificates')
data = pd.read_csv (r'Git and Git-Hub.csv') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'Template.jpg')
    d = ImageDraw.Draw(im)
    fon = ImageFont.truetype("arial.ttf", 60)
    location = (700, 645)
    text_color = (0, 46, 99)
    d.text(location, i, fill = text_color,font=fon ,stroke_width=1)
    cert_dir = '/home/sadi/Certificate generator/certificates/'
    filee=cert_dir+"certificate_" + i + ".pdf"
    im.save(filee)
