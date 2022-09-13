# Вам необходимо написать программу по работе с массивом однотипных данных (например, только числа или
# строки и т.п.). Для этого нужно объявить класс с именем Array, объекты которого создаются командой:
# ar = Array(max_length, cell)
# где max_length - максимальное количество элементов в массиве; cell - ссылка на класс, описывающий отдельный
# элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива (в объектах класса Integer)
# должны быть равны 0.

# Для работы с целыми числами объявите в программе еще один класс с именем Integer, объекты которого создаются командой:
# cell = Integer(start_value)
# где start_value - начальное значение ячейки (в данном случае - целое число).

# В классе Integer должно быть следующее свойство (property):
# value - для изменения и считывания значения из ячейки (само значение хранится в локальной приватной переменной;
# имя придумайте сами).

# При попытке присвоить не целое число должно генерироваться исключение командой:
# raise ValueError('должно быть целое число')
# Для обращения к отдельным элементам массива в классе Array необходимо определить набор магических методов для
# следующих операций:
# value = ar[0] # получение значения из первого элемента (ячейки) массива ar
# ar[1] = value # запись нового значения во вторую ячейку массива ar
# Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно генерироваться
# исключение командой: raise IndexError('неверный индекс для доступа к элементам массива')

# Пример использования классов (эти строчки в программе не писать):
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError




class Array:
    def __init__(self, max_length=0, cell=None):
        self.max_length = max_length
        self.cell = cell
        self.__arr = list(self.cell() for _ in range(self.max_length))

    def __check_index(self, number):
        arr_len = len(self.__arr)
        if not isinstance(number, int) or not 0 <= number < arr_len:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__arr[item].value

    def __setitem__(self, key, number):
        self.__check_index(key)
        self.__arr[key].value = number

    def __str__(self):
        return ' '.join(map(str, self.__arr))


class Integer:
    def __init__(self, start_value=0):
        self.__sv = start_value

    @property
    def value(self):
        return self.__sv

    @value.setter
    def value(self, number):
        if type(number) != int:
            raise ValueError('должно быть целое число')
        self.__sv = number

    def __repr__(self):
        return str(self.__sv)