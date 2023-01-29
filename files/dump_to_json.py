# Напишите код, который переводит словарь d в формат JSON. Результат запишите в файл file.json.


import json

with open("file.json", "w") as f:
    json.dump(d, fp=f)