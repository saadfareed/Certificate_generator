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
    #Attendee name
    fon = ImageFont.truetype("arial.ttf", 60)
    location = (675, 645)
    text_color = (0, 30, 49)
    #location for Attendee name
    d.text(location, i, fill = text_color,font=fon ,stroke_width=2)

    #my name signature
    fox = ImageFont.truetype("PWSignaturetwo.ttf", 50)
    locat = (85, 1000)
    txt_color = (0, 0, 0)
    l="Muhammad Saad Fareed"
    #location for my signature
    d.text(locat, l , fill = txt_color,font=fox ,stroke_width=1)
    #Saving my certificate
    cert_dir = '/home/sadi/Certificate generator/certificates/'
    filee=cert_dir+"certificate_" + i + ".pdf"
    im.save(filee)
