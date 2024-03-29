# Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные
# о студентах некоторого курса:

# [
#    {
#       "name": "Holly-Anne",
#       "city": "Abilene",
#       "age": 29,
#       "progress": 85,
#       "phone": "(802) 983-9126"
#    },
#    ...
# ]

# Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
# name — имя
# city — город проживания
# age — возраст
# progress — прогресс по курсу в процентах
# phone — контактный номер

# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
# возраст 18 лет или более
# прогресс по курсу 75% или более

# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), и записать в него данные
# выбранных студентов, расположив их в лексикографическом порядке имён. В качестве разделителя в файле data.csv должна
# быть использована запятая.


import pandas as pd

pd.read_json('students.json')  \
  .query('age >= 18 and progress >=75') \
  .sort_values(by='name')[['name', 'phone']] \
  .to_csv('data.csv', index=False)