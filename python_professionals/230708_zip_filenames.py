# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00.
# Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
# Примечание 2. Начальная часть ответа выглядит так:
# countries.json
# data_sample.csv
# ...


from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_obj:
    expected_time = datetime(2021, 11, 30, 14, 22, 0)
    file_names = [x.filename.rsplit('/')[-1] for x in zip_obj.infolist() if not x.is_dir() and datetime(*x.date_time) > expected_time]
    print(*sorted(file_names), sep='\n')