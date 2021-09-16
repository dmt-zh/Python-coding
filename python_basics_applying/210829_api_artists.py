# В этой задаче вам необходимо воспользоваться API сайта artsy.net. API проекта Artsy предоставляет информацию
# о некоторых деятелях искусства, их работах, выставках. В рамках данной задачи вам понадобятся сведения о деятелях
# искусства (назовем их, условно, художники). Вам даны идентификаторы художников в базе Artsy. Для каждого
# идентификатора получите информацию о имени художника и годе рождения. Выведите имена художников в порядке неубывания 
# года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

# Работа с API Artsy
# Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа
# к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в 
# дальнейшем все запросы к API осуществляются при помощи этого ключа. Чтобы начать работу с API проекта Artsy, вам 
# необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые
# шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret.
# После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
# как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.


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
