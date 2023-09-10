# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
# в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...

# Напишите программу, которая определяет, сколько раз пользователь менял имя.
# Программа должна вывести адреса электронных почт пользователей, указав для каждого соответствующее количество смененных имен.
# Почтовые ящики должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

# <адрес электронной почты>: <количество изменений имен>



from collections import Counter
import csv

with open('name_log.csv', encoding='utf8') as fin:
    logs = csv.DictReader(fin)
    stats = Counter(map(lambda x: x.get('email'), logs))
    for k, v in sorted(stats.items()):
        print(f'{k}: {v}')