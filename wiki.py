import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = requests.get(articleUrl)
    bs = BeautifulSoup(html.content, 'html.parser')
    # print(bs.prettify())
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('https://en.wikipedia.org/wiki/Ozon.ru')
print(len(links))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    #для генерации сида, чтобы рандом каждый раз был разный
    # print(newArticle)
    newArticle = 'https://en.wikipedia.org/' + newArticle
    print(newArticle)
    links = getLinks(newArticle)
    print(links)
