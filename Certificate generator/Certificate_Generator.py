import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_csv (r'Git and Git-Hub.csv') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'Untitled-1.jpg')
    d = ImageDraw.Draw(im)
    location = (800, 680)
    text_color = (0, 137, 209)
    d.text(location, i, fill = text_color)
    im.save("certificate_" + i + ".pdf")

