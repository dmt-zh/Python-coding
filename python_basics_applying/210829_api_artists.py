import requests
import json

client_id = '*****'
client_secret = '*****'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

# инициируем запрос с заголовком
file_path = 'D:\\coding\\data\\dataset_24476_4.txt'

res = {}

with open(file_path, 'r') as fin:
    for line in fin:
        ids = line.strip()
        r = requests.get(f'https://api.artsy.net/api/artists/{ids}', headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)
        res[j['sortable_name']] = j['birthday']

answer = sorted(res.items(), key=lambda name: (name[1], name[0]))

for artist in answer:
    print(artist[0])

