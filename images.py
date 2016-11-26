#!/usr/bin/env python
import os
from PIL import Image
from colorthief import ColorThief


W, H = 40, 40
DIR = "data/images"
OUTPUT = "data/images_t"
PARTS = "data/images_p"
USER_IMG_PATH = "/home/larleyt/Documents/jubka-tatjanka-2.jpg"


def process_original_images():
    for i in os.listdir(DIR):
        if not i.startswith("."):
            im = Image.open("{}/{}".format(DIR, i))
            im.thumbnail((W, H), Image.ANTIALIAS)
            w, h = im.size
            im = im.crop(box=[w / 3, 0, 2 * w / 3, h])
            head, body, legs, foots = (0, H / 6), (H / 6, H / 2), (H / 2, 5 * H / 6), (5 * H / 6, H)
            head_i, body_i, legs_i, foots_i = 4 * (im.copy(),)
            for _im, pos, part in ((head_i, head, "head"), (body_i, body, "body"), (legs_i, legs, "legs"), (foots_i, foots, "foots")):
                new_im = _im.crop(box=[0, pos[0], _im.size[0], pos[1]])
                new_im.save("{}/{}/{}".format(PARTS, part, i))
            im.save("{}/{}".format(OUTPUT, i))



def find_parts_dominant():
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
    return img_list


def find_user_dominant(img_path):
    color_thief = ColorThief(img_path)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    # palette = color_thief.get_palette(color_count=3)
    
    img_data = {
        "img_path": img_path,
        "dominant_color": dominant_color,
        #"palette": ["#%02x%02x%02x" % color for color in palette]
    }
    return img_data

print(find_user_dominant(USER_IMG_PATH))


def compare_dominants():
    pass
