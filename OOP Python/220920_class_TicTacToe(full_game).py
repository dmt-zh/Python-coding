# Техническое задание

# Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты
# этого класса будут создаваться командой: game = TicTacToe()
# В каждом объекте этого класса должен быть публичный атрибут:
# pole - двумерный кортеж, размером 3x3.

# Каждый элемент кортежа pole является объектом класса Cell: cell = Cell()
# В объектах этого класса должно автоматически формироваться локальное свойство:
# value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

# Также с объектами класса Cell должна выполняться функция:
# bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

# К каждой клетке игрового поля должен быть доступ через операторы:
# res = game[i, j] # получение значения из клетки с индексами i, j
# game[i, j] = value # запись нового значения в клетку с индексами i, j

# Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует
# генерировать исключение командой: raise IndexError('некорректно указанные индексы')
# Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики,
# в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):
# FREE_CELL = 0      # свободная клетка
# HUMAN_X = 1        # крестик (игрок - человек)
# COMPUTER_O = 2     # нолик (игрок - компьютер)

# В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
# init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
# show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
# human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

# Также в классе TicTacToe должны быть следующие объекты-свойства (property):
# is_human_win - возвращает True, если победил человек, иначе - False;
# is_computer_win - возвращает True, если победил компьютер, иначе - False;
# is_draw - возвращает True, если ничья, иначе - False.

# Наконец, с объектами класса TicTacToe должна выполняться функция:
# bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и
# False - в противном случае.

# Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было
# бы сыграть в "Крестики-нолики" между человеком и компьютером.
# P.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.




from random import choice
from itertools import product

class Cell:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return self.value == 0

    def __repr__(self):
        if self.value == 1:
            return 'X'
        if self.value == 2:
            return '0'
        else:
            return '#'


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self, size=3):
        self.__size = size
        self.pole = tuple(tuple(Cell() for _ in range(size)) for _ in range(size))
        self.__free_cells = size ** 2
        self.__human_win = self.__computer_win = self.__draw = False

    def __check_indexes(self, idx):
        r, c = idx
        valid_row = type(r) == int and 0 <= r < self.__size
        valid_col = type(c) == int and 0 <= c < self.__size
        if not (valid_row and valid_col):
            raise IndexError('некорректно указанные индексы')

    def __check_value(self, value):
        if type(value) != int or value not in (0, 1, 2):
            raise TypeError('неверный тип присваиваемых данных')

    def __check_game_state(self, value):
        all_rows = any(all(cell.value == value for cell in row) for row in self.pole)
        all_cols = any(all(cell[col].value == value for cell in self.pole) for col in range(3))
        diagonal1 = all(self.pole[i][j].value == value for i, j in zip(range(3), range(3)))
        diagonal2 = all(self.pole[i][j].value == value for i, j in zip(range(3), range(2, -1, -1)))
        is_winner = any([all_rows, all_cols, diagonal1, diagonal2])
        self.__human_win = True if is_winner and value == 1 else False
        self.__computer_win = True if is_winner and value == 2 else False
        if self.__free_cells == 0 and not self.__human_win and not self.__computer_win:
            self.__draw = True

    def __getitem__(self, item):
        self.__check_indexes(item)
        row, col = item
        return self.pole[row][col].value

    def __setitem__(self, key, value):
        self.__check_indexes(key)
        self.__check_value(value)
        row, col = key
        self.pole[row][col].value = value
        self.__check_game_state(value)

    def __bool__(self):
        return all((not self.__human_win, not self.__computer_win, not self.__draw, self.__free_cells > 0))

    def init(self):
        self.__human_win = self.__computer_win = self.__draw = False
        self.__free_cells = self.__size ** 2
        for row in self.pole:
            for cell in row:
                cell.value = 0

    def human_go(self):
        indx = input("Введите два числа от 0 до 2 через пробел: ").strip().split(' ')
        try:
            row, col = list(map(int, indx))
            cell = self[row, col]
            if cell != 0:
                print('Клетка уже занята, выберите другую :)')
            else:
                self[row, col] = self.HUMAN_X
        except:
            print('Указывайте только целые числа от 0 до 2 через пробел!!!')

    def computer_go(self):
        indexes = tuple((i, j) for i, j in product(range(self.__size), range(self.__size)))
        row, col = choice(indexes)
        cell = self.pole[row][col]
        while not cell:
            row, col = choice(indexes)
            cell = self.pole[row][col]
        self.__free_cells -= 1
        cell.value = self.COMPUTER_O
        self.__check_game_state(self.COMPUTER_O)

    def show(self):
        print('\n'.join(' '.join((str(cell) for cell in arr)) for arr in self.pole))
        print('-*-' * 10)

    @property
    def is_human_win(self):
        return self.__human_win

    @property
    def is_computer_win(self):
        return self.__computer_win

    @property
    def is_draw(self):
        return self.__draw



game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")