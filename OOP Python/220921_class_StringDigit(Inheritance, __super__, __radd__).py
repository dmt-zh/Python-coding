# Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса
# StringDigit должны создаваться командой:

# sd = StringDigit(string)
# где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы
# один не цифровой символ, то генерировать исключение командой:
# raise ValueError("в строке должны быть только цифры")

# Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:
# sd = sd + "123"
# sd = "123" + sd

# создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется
# не цифровой символ, то генерировать исключение:
# raise ValueError("в строке должны быть только цифры")

# Пример использования класса (эти строчки в программе не писать):
# sd = StringDigit("123")
# print(sd)       # 123
# sd = sd + "456" # StringDigit: 123456
# sd = "789" + sd # StringDigit: 789123456
# sd = sd + "12f" # ValueError



class StringDigit(str):
    def __init__(self, string):
        self.__check_values(string)
        super().__init__()

    @staticmethod
    def __check_values(s):
        if not all(n.isdigit() for n in s):
            raise ValueError("в строке должны быть только цифры")

    @staticmethod
    def __check_type(s):
        if type(s) != str:
            raise TypeError("аргументом должнен быть строковый формат содержащий цисла")

    def __add__(self, other):
        self.__check_type(other)
        new_obj = super().__add__(other)
        return StringDigit(new_obj)

    def __radd__(self, other):
        self.__check_type(other)
        new_obj = other.__add__(self)
        return StringDigit(new_obj)