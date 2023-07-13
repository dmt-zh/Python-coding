# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
# всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до
# и после сжатия, в следующем формате:

# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)

# Между данными о двух файлах должна располагаться пустая строка.



from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_obj:
    files_info = [(x.filename.rsplit('/')[-1], datetime(*x.date_time), x.file_size, x.compress_size) for x in zip_obj.infolist() if not x.is_dir()]
    for obj in sorted(files_info, key=lambda x: x[0]):
        print(
            f'{obj[0]}\n  '
            f'Дата модификации файла: {obj[1]}\n  '
            f'Объем исходного файла: {obj[2]} байт(а)\n  '
            f'Объем сжатого файла: {obj[-1]} байт(а)\n'
        )