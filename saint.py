import requests
from bs4 import BeautifulSoup
import json

saints_list = []

_urlsite = requests.get('https://santo.cancaonova.com/santos/') # url initial

content = _urlsite.content

site = BeautifulSoup(content, 'html.parser')

saints = site.find_all('h3')


for s in saints:
    saints_name = s.get_text(strip=True)
    saints_list.append({'name': saints_name})

with open("saints.json", "w", encoding="utf-8") as json_file:
    json.dump(saints_list, json_file, ensure_ascii=False, indent=4)

