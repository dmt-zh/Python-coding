# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время. Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

# Файл с данными:
# Crimes.csv

from collections import Counter
import csv

file_path = 'D:\\coding\\data\\crimes.csv'

crimes = []
with open(file_path) as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        crimes.append(row['Primary Type'])
print(Counter(crimes).most_common()[0])