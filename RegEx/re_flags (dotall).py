# Найдите весь текст от start до end.

# Sample Input 1:
# start
# Каждое
# Слово
# На
# Новой
# Строке
# end

# Sample Output 1:
# ['\nКаждое\nСлово\nНа\nНовой\nСтроке\n']

# Sample Input 2:
# spamstartЭТОТ
# ТЕКСТ
# НАХОДИТСЯ
# НА
# НЕСКОЛЬКИХ
# СТРОКАХ
# endspam

# Sample Output 2:
# ['ЭТОТ\nТЕКСТ\nНАХОДИТСЯ\nНА\nНЕСКОЛЬКИХ\nСТРОКАХ\n']


import re, sys

text = ''.join(sys.stdin.readlines())
print(re.findall(r'(?s)(?<=start).+(?=end)', text))