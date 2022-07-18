# Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
# Этот класс должен иметь следующие методы:
# check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
# если номер в верном формате и False - в противном случае.
# Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).

# check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True,
# если имя записано верно и False - в противном случае.
# Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.



import re

class CardCheck:
    @staticmethod
    def check_card_number(number):
        return bool(re.fullmatch(r'^\d{4}-\d{4}-\d{4}-\d{4}$', number))

    @staticmethod
    def check_name(name):
        return bool(re.fullmatch(r'^[A-Z]+\s[A-Z]+$', name))