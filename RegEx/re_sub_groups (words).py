# Замените два повторяющиеся слова на одно. Если слова одинаковые, но регистр разный - считаем что и слова разные.
#
# Sample Input 1:
# Тут два два слова подряд!

# Sample Output 1:
# Тут два слова подряд!

# Sample Input 2:
# Нужно удалять удалять повторяющиеся слова слова.

# Sample Output 2:
# Нужно удалять повторяющиеся слова.

# Sample Input 3:
# ошибка ошибка

# Sample Output 3:
# ошибка



import re
print(re.sub(r'(\w+)\s\1', r'\1', input()))