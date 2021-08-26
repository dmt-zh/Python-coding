# Вашей программе на вход подается ссылка на HTML файл. Вам необходимо скачать этот файл, затем найти в нем все ссылки
# вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка. Сайтом в данной задаче будем называть
# имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов
# протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками
# вида <a href="../some_path/index.html">. Сайты следует выводить в алфавитном порядке.

# Пример HTML файла:
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">

# Пример ответа:
# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru


url = input()

import requests
import re

link_pattern = r'<a.* href="(?:\w+://){0,1}(\w[\w\.-]+).*"'

res = requests.get(url)
links = list(re.findall(link_pattern, res.text))
for link in sorted(set(links)):
    print(link)
