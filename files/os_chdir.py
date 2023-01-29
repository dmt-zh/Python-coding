# В текущей директории лежит файл path.txt. Он содержит название папки, в которой находится еще один файл path.txt,
# и так далее. Проследуйте по цепочке до конца, пока не найдете пустой файл. Запишите в переменную answer абсолютный
# путь до этой папки.


import os

with open('path.txt') as fin:
    next_folder = fin.read()

while next_folder:
    os.chdir(next_folder)

    with open('path.txt') as f:
        next_folder = f.read()

answer = os.getcwd()