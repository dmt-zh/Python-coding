# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.


import requests

file_path = 'D:\\dataset_3378_3.txt'
pattern = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open(file_path, 'r') as fin:
    r = requests.get(fin.readline().strip())
    link = r.text
while str(link[:2]) != 'We':
    url = pattern + link
    req = requests.get(url)
    link = req.text.strip()
    print(link)