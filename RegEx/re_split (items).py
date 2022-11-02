# На вход даётся большой текст. Используйте re.split() для того, чтобы убрать категории и оставить только товары.
# Товары выведите построчно.

# Sample Input 1:
# Категория: Телефоны\nSupreme Burner\nMotorola Razr\nКатегория: Смарт часы и браслеты\n
# Apple Watch 6\nGarmin Venu\nXiaomi Mi Smart Band 6\nКатегория: Игры\nSpore

# Sample Output 1:
# Supreme Burner
# Motorola Razr
# Apple Watch 6
# Garmin Venu
# Xiaomi Mi Smart Band 6
# Spore


import re

raw_items = re.split(r'Категория: .+?\\n|\\n', input())
items = list(filter(lambda x: len(x) > 0, raw_items))
print(*items, sep='\n')