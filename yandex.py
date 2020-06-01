import requests
from bs4 import BeautifulSoup

payload = {"text": "ozon", "lr": 213}
r = requests.get("https://yandex.ru/search/", params=payload)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
# print(r.content)

with open("result.txt", 'a') as file:
    for link in soup.find_all("a"):
        file.write(link.get('href') + "\n")