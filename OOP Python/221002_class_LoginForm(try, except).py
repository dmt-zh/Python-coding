# Объявите класс с именем ValidatorString, объекты которого создаются командой:
# vs = ValidatorString(min_length, max_length, chars)
# где min_length, max_length - минимально и максимально допустимая длина строки (целые числа,
# формируемые диапазон [min_length; max_length]); chars - строка из набора символов (хотя бы
# один из них должен присутствовать в проверяемой строке). Если chars - пустая строка, то проверку
# на вхождение символов не делать.

# В самом классе ValidatorString объявите метод:
# def is_valid(self, string): ... который проверяет строку string на соответствие критериям: string должна
# быть строкой, с длиной в диапазоне [min_length; max_length] и в string присутствует хотя бы один символ
# из chars. Если хотя бы один из этих критериев не выполняется, то генерируется исключение командой:
# raise ValueError('недопустимая строка')

# Затем, объявите класс с именем LoginForm, объекты которого создаются командой:
# lg = LoginForm(login_validator, password_validator)
# где login_validator - валидатор для логина (объект класса ValidatorString); password_validator - валидатор
# для пароля (объект класса ValidatorString).

# В самом классе LoginForm объявите следующий метод:
# def form(self, request): ... где request - объект запроса (словарь). В словаре request должен быть ключ
# 'login' со значением введенного логина (строки) и ключ 'password' со значением введенного пароля (строка).
# Если хотя бы одного ключа нет, то генерировать исключение командой:
# raise TypeError('в запросе отсутствует логин или пароль')

# В противном случае (если проверка для request прошла), проверять корректность полученного формой логина
# и пароля с помощью валидаторов, указанных в параметрах login_validator и password_validator, при создании
# объекта формы.

# Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password
# присвоить соответствующие значения.



class ValidatorString:
    def __init__(self, min_length=0, max_length=10, chars=''):
        self.__min_length = min_length
        self.__max_length = max_length
        self.__chars = chars

    def __setattr__(self, key, value):
        if key in ('__min_length', '__max_length'):
            if type(value) != int or value < 0:
                raise AttributeError('значения "min_length" и "max_length" должны быть целыми положительнми числами!')
        if key == '__chars':
            if type(value) != str:
                raise AttributeError('тип параметра chars должн быть строковым!')

        object.__setattr__(self, key, value)

    def is_valid(self, string):
        valid_len = self.__min_length <= len(string) <= self.__max_length
        has_chars = any(map(lambda x: x in string, self.__chars)) if self.__chars != '' else True
        if not (valid_len and has_chars):
            raise ValueError('недопустимая строка')
        return string


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.__login_validator = login_validator
        self.__password_validator = password_validator
        self._login = self._password = None

    def form(self, request):
        valid_type = isinstance(request, dict)
        login, password = request.get('login', False), request.get('password', False)

        if not (valid_type and all((login, password))):
            raise TypeError('в запросе отсутствует логин или пароль')

        self._login = self.__login_validator.is_valid(login)
        self._password = self.__password_validator.is_valid(password)


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
