#!/usr/bin/env python
import os
import json
import requests

API_URL = 'https://api.zalando.com/'


# GET THIS FROM AN IMAGE
IMAGE_TXT = "a man in a suit and tie walking down a street ."


ctx = {}


class ZalandoAPI():
    WOMEN = "WOMEN"
    MEN = "MEN"
    KIDS = "KIDS"
    SEX_KEY = "targetGroup"
    CATEGORIES_KEY = "categoryKeys"

    def api_call(self, method, request_method="GET", extra_data=None):
        if extra_data is None:
            extra_data = {}
        return requests.get(API_URL + method, params=extra_data).json()

    def categories(self, extra_data=None):
        return self._categories(extra_data)["content"]

    def _categories(self, extra_data=None):
        return self.api_call("categories", extra_data=extra_data)

    def articles(self, extra_data=None):
        return self.api_call("articles", extra_data=extra_data)["content"]


api = ZalandoAPI()

MEN = {i: api.MEN for i in ["man", "male"]}
WOMEN = {i: api.WOMEN for i in ["woman", "female"]}
KIDS = {i: api.KIDS for i in ["boy", "girl"]}

SEX = {}
SEX.update(MEN)
SEX.update(WOMEN)
SEX.update(KIDS)


def get_categories():
    CACHE_FILE_NAME = "cache/categories.json"
    if not os.path.isfile(CACHE_FILE_NAME):
        f = open(CACHE_FILE_NAME, "w")
        total_pages = int(api._categories()["totalPages"])
        categories = []
        for page in range(1, total_pages + 1):
            categories += api.categories({"page": page})
        f.write(json.dumps(categories))
        f.close()
    return json.loads(open(CACHE_FILE_NAME).read())


CATEGORIES = {category["name"]: category["key"] for category in get_categories()}


def get_image_text(image_file=None):
    return IMAGE_TXT


def get_image_meta_info(image_text):
    for word in image_text.lower().strip().split():
        sex = SEX.get(word)
        categories = CATEGORIES.get(word)
        if categories:
            ctx.update({api.CATEGORIES_KEY: categories})
        if sex:
            ctx.update({api.SEX_KEY: sex})
    return ctx


def do_recommend(image_file=None):
    image_text = get_image_text(image_file)
    meta_info = get_image_meta_info(image_text)
    print meta_info

    result = api.categories(meta_info)
    result = map(lambda i: i.get("name"), result)
    return result


def get_word_power(word):
    l = len(word)
    affix = word[:3]
    suffix = word[:3]
    fr = to = 3



if __name__ == "__main__":
    results = do_recommend(None)
    print results
