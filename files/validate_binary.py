# Напишите программу, которая считывает файл file.pickle. Не забудьте, что в файле может содержаться
# вредоносный код, поэтому вы перед считыванием содержимого обязательно должны проверить сигнатуру файла.
# Ключ и сигнатура хранятся в файле secrets.txt в разных строках.
# В случае если сигнатура верная – достаньте из файла file.pickle словарь и добавьте в него новый ключ answer со
# значением easy pickle.

# Если же сигнатура неверная – создайте новый словарь c ключом answer и значением not correct.
# Полученный словарь запишите в файл answer.json.


import pickle
import hmac
import hashlib
import json


with open('secrets.txt') as f_sec:
    secret_key = f_sec.readline().strip()
    sha_key = f_sec.readline().strip()

with open('file.pickle', 'rb') as fin, open("answer.json", "w") as fout:
    raw_data = fin.read()
    expected_key = hmac.new(bytes(secret_key, 'utf8'), raw_data, hashlib.sha256).hexdigest()

    if expected_key == sha_key:
        unpickled = pickle.loads(raw_data)
        unpickled['answer'] = 'easy pickle'
        json.dump(unpickled, fp=fout)
    else:
        json.dump({'answer': 'not correct'}, fp=fout)