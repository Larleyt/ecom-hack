import os
from colorthief import ColorThief

dominant_color = []
palette = []
DIR = "data/images_t"

img_list = []

for img_file in os.listdir(DIR):
    img_data = {}
    if not img_file.startswith('.'):
        img_path = "{}/{}".format(DIR, img_file)
        color_thief = ColorThief(img_path)
        # get the dominant color
        dominant_color = color_thief.get_color(quality=5)
        # build a color palette
        # palette = color_thief.get_palette(color_count=3)
        
        img_data.update({
            "img_path": img_file,
            "dominant_color": dominant_color,
            #"palette": ["#%02x%02x%02x" % color for color in palette]
        })
        img_list.append(img_data)

print(img_list)
