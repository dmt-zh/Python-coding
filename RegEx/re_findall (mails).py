# Дана строка с текстом. Вам нужно вывести все почты, которые там есть. Гарантируется, что перед
# началом каждой почты стоит пробел.
# В задаче расматриваются адреса с окончанием .com и .ru.

# Sample Input 1:
# test mihryutkamihryutka1@gmail.comвфывфывфывфывфывф serginio1963@gmail.comru velesgod111@gmail.comru
# ofice_plus@mail.rucom borisbaranob46@gmail.comdasdasda bradley@automatedmarine.comввыф fddsfwfwefwdfwd@mail.ru

# Sample Output 1:
# mihryutkamihryutka1@gmail.com
# serginio1963@gmail.com
# velesgod111@gmail.com
# ofice_plus@mail.ru
# borisbaranob46@gmail.com
# bradley@automatedmarine.com
# fddsfwfwefwdfwd@mail.ru



import re

mails = re.findall(r'(?<=\s)\w+-*\w+@\w+\.(?:com|ru)', input())
print(*mails, sep='\n')
