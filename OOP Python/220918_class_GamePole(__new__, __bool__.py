# Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем.
# Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell
# и содержать либо число мин вокруг этой клетки, либо саму мину.

# Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого
# класса должен формироваться командой:
# pole = GamePole(N, M, total_mines)

# И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте
# паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

# Объект pole должен иметь локальный приватный атрибут:
# __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из
# объектов класса Cell.

# Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):
# pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

# Далее, в самом классе GamePole объявите следующие методы:
# init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
# open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение
# атрибута __is_open объекта Cell в ячейке (i, j) на True;
# show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее
# задание).

# Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint
# модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет
# мин). Область охвата - соседние (прилегающие) клетки (8 штук).

# В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то
# генерируется исключение командой:
# raise IndexError('некорректные индексы i, j клетки игрового поля')

# Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:
# cell = Cell()

# При этом в самом объекте создаются следующие локальные приватные свойства:
# __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
# __number - число мин вокруг клетки (целое число от 0 до 8);
# __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

# Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:
# is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;
# is_open - для записи и чтения информации из атрибута __is_open.

# В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение
# True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение
# командой: raise ValueError("недопустимое значение атрибута")

# С объектами класса Cell должна работать функция:
# bool(cell)
# которая возвращает True, если клетка закрыта и False - если открыта.




from itertools import product
from random import randint

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    def __check_attr(self, attr, number=True):
        if number:
            valid = isinstance(attr, int) and 0 <= attr < 9
        else:
            valid = isinstance(attr, bool)
        if not valid:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        self.__check_attr(value, number=False)
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__check_attr(value)
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        self.__check_attr(value, number=False)
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open

    def __repr__(self):
        if self:
            return '#'
        else:
            if self.__is_mine:
                return '*'
            return str(self.__number)


class GamePole:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.__rows = N
        self.__cols = M
        self.__mins = total_mines
        self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        rows_border = self.__rows - 1
        cols_border = self.__cols - 1
        mins_left = self.__mins
        mins_coords = []
        while mins_left != 0:
            row, col = randint(0, rows_border), randint(0, cols_border)
            if not (row, col) in mins_coords:
                mins_coords.append((row, col))
                self.__pole_cells[row][col].is_mine = True
                mins_left -= 1

                row_start = row - 1 if row > 0 else 0
                row_end = row + 1 if row < rows_border else rows_border

                col_start = col - 1 if col > 0 else 0
                col_end = col + 1 if col < cols_border else cols_border

                for idx_row, idx_col in product(range(row_start, row_end + 1), range(col_start, col_end + 1)):
                    if (row, col) != (idx_row, idx_col):
                        cell = self.__pole_cells[idx_row][idx_col]
                        cell.number += 1
        return None

    def open_cell(self, i, j):
        valid_row = 0 <= i < self.__rows
        valid_col = 0 <= j < self.__cols
        if not (valid_row and valid_col):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        print('\n'.join(' '.join(map(str, cell)) for cell in self.__pole_cells))