# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов. Вам необходимо распаковать этот
# архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
# Для лучшего понимания формата задачи, ознакомьтесь с примером.

# Solution one:

import os
folder = 'D:\\coding\\data\\main'

with open('D:\\coding\\data\\res.main.txt', 'w') as fout:
    for cur_dir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                fout.write(cur_dir.replace("D:\coding\data\\", '').replace('\\', '/') + '\n')
                break



# Solution two:

from zipfile import ZipFile
import re

file_name = 'D:\\coding\\data\\main.zip'

res = set()

with ZipFile(file_name, 'r') as zip:
    lst = zip.namelist()
    for dirs in lst:
        if dirs.endswith('.py'):
            dirs = re.sub('\/\w+\.[py]+$', '', dirs)
            res.add(dirs + '\n')

with open('D:\\coding\\data\\res.main.txt', 'w') as fout:
    for line in sorted(res):
        fout.write(line)