# Создается проект, в котором предполагается использовать списки из целых чисел.
# Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list
# и переопределить три метода:

# __init__()
# __setitem__()
# append()

# так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных,
# генерировать исключение командой:
# raise TypeError('можно передавать только целочисленные значения')

# Пример использования класса ListInteger (эти строчки в программе не писать):
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError



class ListInteger(list):
    def __init__(self, args):
        for x in args:
            self.__check_value(x)
        super().__init__(args)

    @staticmethod
    def __check_value(value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_value(value)
        super().__setitem__(key, value)

    def append(self, item):
        self.__check_value(item)
        super().append(item)