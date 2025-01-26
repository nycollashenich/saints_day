import requests
from bs4 import BeautifulSoup

response = requests.get('https://santo.cancaonova.com/santos/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# print(site.prettify())  # prettify = indentação

li = site.find('a', attrs={'class': 'thumbnail thumbnail-left'})
# print(li.prettify())


sant_name = li.find('h3')
# print(sant_name.text)

sant_resume = li.find('p')
print(sant_resume.text)