# Объявите два класса:
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.

# С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False),
# означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться
# локальные свойства:

# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).


# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса
# Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

# В классе GamePole должны быть также реализованы следующие методы:
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая
# мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается
# символ #).


# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной
# инициализации игрового поля.

# В классе GamePole могут быть и другие вспомогательные методы.
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.




from itertools import product
import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def __repr__(self):
        if not self.fl_open:
            return '#'
        else:
            if self.mine:
                return '*'
            return str(self.around_mines)


class GamePole:
    def __init__(self, N, M):
        self.pole = self.init(N, M)

    def init(self, size, mins_number):
        left_border = size - 1
        grid = [[Cell() for _ in range(size)] for _ in range(size)]
        mins_left = mins_number
        mins_coords = []
        while mins_left != 0:
            coords = random.randint(0, left_border), random.randint(0, left_border)
            if not coords in mins_coords:
                mins_coords.append(coords)
                grid[coords[0]][coords[1]].mine = True
                mins_left -= 1
        self.__fill_grid(mins_coords, grid, left_border)
        return grid

    @staticmethod
    def __fill_grid(mine_coords, grid, left_border):
        for coords in mine_coords:
            coord1_start = coords[0] - 1 if coords[0] > 0 else 0
            coord1_end = coords[0] + 1 if coords[0] < left_border else left_border

            coord2_start = coords[1] - 1 if coords[1] > 0 else 0
            coord2_end = coords[1] + 1 if coords[1] < left_border else left_border

            for row, col in product(range(coord1_start, coord1_end + 1), range(coord2_start, coord2_end + 1)):
                if (row, col) != coords:
                    cell = grid[row][col]
                    cell.around_mines += 1

    def show(self):
        return '\n'.join(' '.join(map(str, cell)) for cell in self.pole)



pole_game = GamePole(10, 12)
