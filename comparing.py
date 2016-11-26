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

    def api_call(self, method, request_method="GET", **kwargs):
        return requests.get(API_URL + method).json()

    def categories(self, extra_data):
        if not extra_data:
            extra_data = {}
        return self.api_call("categories", extra_data)["content"]


api = ZalandoAPI()

MEN = {i: api.MEN for i in ["man", "male"]}
WOMEN = {i: api.WOMEN for i in ["woman", "female"]}
KIDS = {i: api.KIDS for i in ["boy", "girl"]}

SEX = {}
SEX.update(MEN)
SEX.update(WOMEN)
SEX.update(KIDS)


def get_image_text(image_file=None):
    return IMAGE_TXT


def get_image_meta_info(image_text):
    for word in image_text.lower().strip().split():
        sex = SEX.get(word)
        if sex:
            ctx.update({api.SEX_KEY: sex})
    return ctx


def do_recommend(image_file=None):
    image_text = get_image_text(image_file)
    meta_info = get_image_meta_info(image_text)
    result = api.categories(meta_info)
    result = map(lambda i: i.get("name"), result)
    print(result)
    return result


if __name__ == "__main__":
    do_recommend(None)
