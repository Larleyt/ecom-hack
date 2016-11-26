from colorthief import ColorThief


color_thief = ColorThief('/home/larleyt/fl/web/going_on/ecom-hack/img_00000028.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=3)

print("#%02x%02x%02x" % dominant_color)
for color in palette:
    print("#%02x%02x%02x" % color)
