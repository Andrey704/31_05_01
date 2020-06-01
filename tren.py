import  requests

payload = {'lr': 227, 'text': 'ozon'} # аргументы гет запроса
r = requests.get("https://httpbin.org/get", params=payload)

print(r.text)