# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов,
# каждый из которых содержит информацию о каком-либо футболисте:

# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }

# У футболиста имеются следующие атрибуты:
# first_name — имя
# last_name — фамилия
# team — название футбольного клуба
# position — игровая позиция

# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
# выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен,
# а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.


from zipfile import ZipFile
import json

with ZipFile('data.zip') as zip_obj:
    all_players = []
    json_files = [x for x in zip_obj.namelist() if '.json' in x]
    for file in json_files:
        with zip_obj.open(file) as fin:
            try:
                db = json.loads(fin.read().decode('utf8'))
                if db.get('team') == 'Arsenal':
                    all_players.append(f'{db.get("first_name")} {db.get("last_name")}')
            except:
                continue

    print(*sorted(all_players), sep='\n')