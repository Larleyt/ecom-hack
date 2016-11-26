#!/usr/bin/env python
import os
from PIL import Image

W, H = 40, 40
DIR = "data/images"
OUTPUT = "data/images_t"
PARTS = "data/images_p"

for i in os.listdir(DIR):
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
