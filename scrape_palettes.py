# from lxml import html
# import requests


# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)

# #This will create a list of buyers:
# palette = tree.xpath('/a[@class="palette"]')
# print(palette)


import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
page = http.request('GET', 'http://www.colourlovers.com/fashion/palettes')
soup = BeautifulSoup(page.data)
soup.prettify()
for anchor in soup.findAll("a", { "class" : "palette" }):
    print(anchor)