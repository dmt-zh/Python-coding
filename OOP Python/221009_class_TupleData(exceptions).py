# Вам поручается разработать класс TupleData, элементами которого могут являются только объекты
# классов: CellInteger, CellFloat и CellString.
# Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:
# cell_1 = CellInteger(min_value, max_value)
# cell_2 = CellFloat(min_value, max_value)
# cell_3 = CellString(min_length, max_length)
# где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length,
# max_length - минимальная и максимальная допустимая длина строки в ячейке.

# В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value
# или _min_length, _max_length и соответствующими значениями.

# Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:
# value - для записи и считывания значения в ячейке (изначально возвращает значение None).

# Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length],
# то генерируется исключения командами:
# raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
# raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
# raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString

# Все три класса исключений должны быть унаследованы от одного общего класса: CellException
# Далее, объявите класс TupleData, объекты которого создаются командой:
# ld = TupleData(cell_1, ..., cell_N)
# где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

# Обращение к отдельной ячейке должно выполняться с помощью оператора:
# value = ld[index] # считывание значения из ячейке с индексом index
# ld[index] = value # запись нового значения в ячейку с индексом index
# Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом.
# Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.

# Также с объектами класса TupleData должны выполняться следующие функции и операторы:
# res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
# for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
#     print(d)




class CellException(Exception):
    pass

class CellIntegerException(CellException):
    pass

class CellFloatException(CellException):
    pass

class CellStringException(CellException):
    pass



class Cell:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, '_' + key, value)
        self._value = None

    def _is_valid(self, obj):
        raise NotImplementedError("метод '_is_valid' должен быть реализован в дочернем классе")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, obj):
        self._value = self._is_valid(obj)


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, obj):
        if not type(obj) == int or not self._min_value <= obj <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        return obj


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, obj):
        if not type(obj) == float or not self._min_value <= obj <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        return obj


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _is_valid(self, obj):
        if not type(obj) == str or not self._min_length <= len(obj) <= self._max_length:
            raise CellStringException('значение выходит за допустимый диапазон')
        return obj


class TupleData:
    def __init__(self, *args):
        self._cells = tuple(map(self.__is_cell, args))

    def __is_cell(self, cell):
        if not isinstance(cell, (CellInteger, CellFloat, CellString)):
            raise TypeError('Объектами "TupleData" могут быть только классы унаследованные от класса "Cell"')
        return cell

    def __getitem__(self, item):
        return self._cells[item].value

    def __setitem__(self, key, val):
        self._cells[key].value = val

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        for cell in self._cells:
            yield cell.value
