# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит единственное число — количество файлов в этом архиве.


from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_obj:
    info = zip_obj.infolist()
    print(sum(1 for elem in info if not elem.is_dir()))