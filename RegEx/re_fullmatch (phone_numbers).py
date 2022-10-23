# Очень часто номера телефонов вводят по-разному. Иногда ставят скобки, иногда тире, иногда пробелы,
# иногда вообще ничего не ставят.

# Найдите все валидные номера телефонов:
# Номер может начинаться с 8, 7, +7.
# Разделителями могут быть: пробелы, тире, круглые скобки.
# В номере должно быть 11 цифр.

# Если телефон валидный - выводите True, иначе - False.

# Sample Input 1:
# 7(977)8179710
# Sample Output 1:
# True

# Sample Input 2:
# +79786655917
# Sample Output 2:
# True

# Sample Input 3:
# 89175643308
# Sample Output 3:
# True

# Sample Input 4:
# +89786655917
# Sample Output 4:
# False



import re

class PhoneValidatar:
    def __init__(self, pattern_string):
        self.__pattern = re.compile(pattern_string)

    def __call__(self, phone):
        is_valid = re.fullmatch(self.__pattern, phone)
        return bool(is_valid)


validator = PhoneValidatar('(?:[78]|\+7)(?:[\s\-()]*\d){10}')
print(validator(input()))