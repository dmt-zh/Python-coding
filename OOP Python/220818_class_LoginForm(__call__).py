# Предположим, мы разрабатываем класс для обработки формы авторизации на стороне сервера.
# Для этого был создан следующий класс с именем LoginForm:

# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""
#
#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")
#
#     def is_validate(self):
#         if not self.validators:
#             return True
#
#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False
#
#         return True


# Здесь name - это заголовок формы (строка); validators - список из валидаторов для проверки корректности поля.
# В методе post параметр request - это словарь с ключами 'login' и 'password' и значениями (строками) для логина и пароля
# соответственно.


# Вам необходимо в программе объявить классы валидаторов:
# LengthValidator - для проверки длины данных в диапазоне [min_length; max_length];
# CharsValidator - для проверки допустимых символов в строке.

# Объекты этих классов должны создаваться командами:
# lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина;
# max_length - максимально допустимая длина
# cv = CharsValidator(chars) # chars - строка из допустимых символов

# Для проверки корректности данных каждый валидатор должен вызываться как функция:
# res = lv(string)
# res = cv(string)
# и возвращать True, если string удовлетворяет условиям валидатора и False - в противном случае.



class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.__min_len = min_length
        self.__max_len = max_length

    def __call__(self, strng, *args, **kwargs):
        return type(strng) == str and self.__min_len <= len(strng) <= self.__max_len


class CharsValidator:
    def __init__(self, valid_chars):
        self.__chars = valid_chars

    def __call__(self, strng, *args, **kwargs):
        return set(strng).issubset(self.__chars)