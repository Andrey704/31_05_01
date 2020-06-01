import requests
from bs4 import BeautifulSoup
import re
import os

URL = input("Введите URL, который вы хотитет спарсить: \n")
name_folder = input("Введите название папки: \n")
os.mkdir(name_folder)
page = requests.get(URL.strip())

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

results = soup.find_all('img', src=re.compile('\/\w+\/\d+\/\w+\.jpg'))
print(results)

print(type(results))
print(len(results))


for i in range(len(results)):
    #проходим по каждому элементу нашего сета
    link = results[i]['src']
    # в link у нас лежит относительный путь на картинку на сайте
    print(link)
    img_data = requests.get("https://www.combook.ru"+link)
    # https://www.combook.ru/imgrab/0001/12002157_nviss_0.jpg

    with open(name_folder + "/" + str(i) + ".jpg", "wb") as handler:
        handler.write(img_data.content)

