# Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики".
# Для этого требуется объявить класс TicTacToe (крестики-нолики), объекты которого создаются командой:
# game = TicTacToe()

# Каждый объект game должен иметь публичный атрибут:
# pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

# Каждая клетка игрового поля представляется объектом класса Cell и создается командой:
# cell = Cell()

# Объекты класса Cell должны иметь следующие публичные локальные атрибуты:
# is_free - True, если клетка свободна; False в противном случае;
# value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

# Также с каждым объектом класса Cell должна работать функция: bool(cell)
# которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.

# Класс TicTacToe должен иметь следующий метод:
# clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

# А объекты этого класса должны иметь следующую функциональность (обращение по индексам):
# game[0, 0] = 1 # установка нового значения, если поле закрыто
# res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)

# Если указываются некорректные индексы, то должно генерироваться исключение командой:
# raise IndexError('неверный индекс клетки')

# Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:
# raise ValueError('клетка уже занята')

# Также должны быть реализованы следующие полные срезы при обращении к клеткам игрового поля:
# slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
# slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx




class Cell:
    def __init__(self, is_free=True, value=0):
        self.is_free = is_free
        self.value = value

    def __bool__(self):
        return self.is_free

    def __repr__(self):
        return str(self.value)


class TicTacToe:
    def __init__(self, cell=Cell):
        self.pole = tuple(tuple(cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for c in row:
                c.is_free = True
                c.value = 0

    @staticmethod
    def __indexes(idexes):
        row, col = idexes[0], idexes[1]
        valid_col = (type(col) == int and col < 3) or type(col) == slice
        valid_row = (type(row) == int and row < 3) or type(row) == slice
        if valid_col and valid_row:
            return row, col
        raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        row, col = self.__indexes(item)
        if type(row) == slice:
            return tuple(c[col].value for c in self.pole[row])
        if type(col) == slice:
            return tuple(c.value for c in self.pole[row])
        return self.pole[row][col].value

    def __setitem__(self, key, new_value):
        row, col = self.__indexes(key)
        cell = self.pole[row][col]
        if not cell:
            raise ValueError('клетка уже занята')
        cell.value = new_value
        cell.is_free = False

    def __str__(self):
        return '\n'.join(' '.join(map(str, arr)) for arr in self.pole)