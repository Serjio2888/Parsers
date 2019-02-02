import requests
import re

url = 'https://vk.com/search?c%5Bage_from%5D=18&c%5Bage_to%5D=21&c%5Bcity%5D=119&c%5Bcountry%5D=1&c%5Bgroup%5D=146657779&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people'
r = requests.get(url)
with open('group.txt', 'w') as f:
    f.write(r.text)

with open('group.txt', 'r') as k:
    for i in k:
        if 'class="simple_fit_item search_item">' in i and '</a><a href="/' in i:
            print ((re.split(r'"', i))[1][1:])
