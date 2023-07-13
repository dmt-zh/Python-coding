# ам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит его файловую структуру и объем каждого файла.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде.
# Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

# Примечание 1. Вывод на примере архива test.zip из конспекта:
# test
#   Картинки
#     1.jpg 88 KB
#     avatar.png 19 KB
#     certificate.png 43 KB
#     py.png 33 KB
#     World_Time_Zones_Map.png 2 MB
#     Снимок экрана.png 11 KB
#   Неравенства.djvu 5 MB
#   Программы
#     image_util.py 5 KB
#     sort.py 61 B
#   Разные файлы
#     astros.json 505 B

# Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.


from zipfile import ZipFile


def human_size(byt: int):
    d = {1024 ** 3: 'GB', 1024 ** 2: 'MB', 1024: 'KB', 1: 'B', -1: ''}
    for key, val in d.items():
        if byt > key:
            return f'{round(byt / key)} {val}'

with ZipFile('desktop.zip') as zip_obj:
    for obj in zip_obj.infolist():
        file_ = obj.filename.strip('/').split('/')
        prefix = '' if obj.is_dir() else f' {human_size(obj.file_size)}'
        print(f'{"  " * (len(file_) - 1)}{file_[-1]}{prefix}')