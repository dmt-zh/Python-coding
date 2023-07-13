# Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла

# Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни
# одного названия файла для извлечения, то функция должна извлечь все файлы из архива.

# Примечание. Например, следующий вызов функции
# extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
# должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.

# Вызов функции
# extract_this('workbook.zip')
# должен извлечь из архива workbook.zip все файлы в папку с программой.


from zipfile import ZipFile

def extract_this(archive, *args):
    with ZipFile(archive) as zip_obj:
        zip_obj.extractall(members=args or None)