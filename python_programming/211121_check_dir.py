# На вход подаётся полный путь к файлу относительно текущего каталога.
# Проверьте есть ли такой файл (и файл ли это) и если он есть - выведите содержимое. Иначе выведите одну из 2 ошибок.

# Sample Input 1:
# tmp/dir/text.txt

# Sample Output 1:
# CONTENT:
# Привет, Мир!

# Sample Input 2:
# tmp/dir/

# Sample Output 2:
# ERROR:
# Это каталог, а не файл

# Sample Input 3:
# tmp/text.txt

# Sample Output 3:
# ERROR:
# Файл не существует

import os.path
path = input().strip()

if os.path.isdir(path):
    print(f'ERROR:\nЭто каталог, а не файл')
elif not os.path.isfile(path):
    print(f'ERROR:\nФайл не существует')
else:
    with open(path, 'r', encoding='utf-8') as fout:
        print("CONTENT:", fout.read(), sep="\n")