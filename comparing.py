import json, requests

url = 'https://api.zalando.com/categories'


# GET THIS FROM AN IMAGE
s = "a man in a suit and tie walking down a street ."


ctx = {}

MEN = ["man", "male"]
WOMEN = ["woman", "female"]
KIDS = ["boy", "girl"]


def define_sex(s, ctx):
    for word in s.strip().split():
        if word in MEN:
            ctx.update({"targetGroup": "MEN"})
        elif word in WOMEN:
            ctx.update({"targetGroup": "WOMEN"})
        elif word in KIDS:
            ctx.update({"targetGroup": "KIDS"})
    return ctx

def exclude_similar_cats(s, ctx):
    for 