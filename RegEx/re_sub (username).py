# Напишите программу, которая убирает username пользователей, каналов, ботов в телеграм.
# В username используются символы a-z, 0-9, _. Его длина от 5 до 32 символов.

# Sample Input 1:
# Привет, вот тут мои фотки - @photos_bot

# Sample Output 1:
# Привет, вот тут мои фотки -

# Sample Input 2:
# Я покупала у девочки, меня не обманули, цены за 1 месяц всего 60-70 руб,очень радует это.
# Кому нужен контакт, в телеграме ник @ex4mpl3 Вссем удачи))

# Sample Output 2:
# Я покупала у девочки, меня не обманули, цены за 1 месяц всего 60-70 руб,очень радует это. Кому нужен контакт,
# в телеграме ник  Вссем удачи))

# Sample Input 3:
# @\testttt @+testttt @-testttt @|testttt @?testttt

# Sample Output 3:
# @\testttt @+testttt @-testttt @|testttt @?testttt



import re
cleaned = re.sub(r'@[a-z_\d]{5,32}\b', '', input())
print(cleaned)