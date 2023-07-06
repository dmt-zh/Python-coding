# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах,
# в следующем формате:

# Объем исходных файлов: <объем до сжатия> байт(а)
# Объем сжатых файлов: <объем после сжатия> байт(а)


from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_obj:
    init_size = sum([x.file_size for x in zip_obj.infolist()])
    comp_size = sum([x.compress_size for x in zip_obj.infolist()])
    print(f'Объем исходных файлов: {init_size} байт(а)\nОбъем сжатых файлов: {comp_size} байт(а)')