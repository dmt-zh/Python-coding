# Напишите регулярное выражение, которое найдёт всё содержимое тегов p.
# Нужно найти теги, подходящие по следующим условиям:

# В начале тега стоит:
# <p
# Тут может быть последовательность символов минимально возможной длины
# >
# Внутри тега последовательность из любых символов минимально возможной длины
# В конце тега стоит </p>

# Sample Input 1:
# <noscript class="noscript"><p class="l-header">Сайт не работает<br>без JavaScript 😕</p></noscript>

# Sample Output 1:
# Сайт не работает<br>без JavaScript 😕

# Sample Input 2:
# <p>Это параграф</p>

# Sample Output 2:
# Это параграф

# Sample Input 3:
# <main><section class="faq__section content"><h2 class="h-header">Частозадаваемые вопросы</h2><div class="faq__megawrapper">
# <div class="faq__wrapper"><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">
# Какой-то ответ</p></details><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">
# Какой-то ответ</p></details><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">Какой-то
# Sample Output 3:
# Какой-то ответ
# Какой-то ответ

# Sample Input 4:
# <p Неправильный параграф</p></p>1</p><p>2</p><p3/p>

# Sample Output 4:
# 2


import re
match = re.findall(r'<p[^/>]*?>(.+?)</p>', input())
print(*match, sep='\n')