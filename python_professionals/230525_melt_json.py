# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях:

# [
#    {
#       "country": "Afghanistan",
#       "religion": "Islam"
#    },
#    {
#       "country": "Albania",
#       "religion": "Islam"
#    },
#    ...
# ]

# Каждый объект из этого списка содержит два атрибута:

# country — страна
# religion — исповедуемая религия
# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии,
# а в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна
# записать в файл religion.json.

# Примечание 1. Страны в списках должны располагаться в своем исходном порядке.
# Примечание 2. Начальная часть файла religion.json выглядит так:
# {
#    "Islam":[
#       "Afghanistan",
#       "Albania",
#       "Algeria",
#       ...
#    ],
#    ...
# }




import json
from collections import OrderedDict


def melt_json_file(json_file, output_json_name):

    with open(json_file) as fin, open(output_json_name, 'w', encoding='utf-8') as fout:
        data = json.load(fin)
        religions = OrderedDict()
        for pair in data:
            religions.setdefault(pair.get('religion', 'Not found'), []).append(pair.get('country'))
        json.dump(religions, fout, indent=3)

melt_json_file('countries.json', 'religion.json')
