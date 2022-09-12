# Вам необходимо для навигатора реализовать определение маршрутов. Для этого в программе
# нужно объявить класс Track, объекты которого создаются командой:
# tr = Track(start_x, start_y)
# где start_x, start_y - координата начала пути.

# В этом классе должен быть реализован следующий метод:
# add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент), который можно пройти со
# средней скоростью speed.

# Также с объектами класса Track должны выполняться команды:
# coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и скорости (число) для линейного
# сегмента маршрута с индексом indx
# tr[indx] = speed # изменение средней скорости линейного участка маршрута по индексу indx
# Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - число линейных сегментов
# в маршруте), то генерируется исключение командой: raise IndexError('некорректный индекс')





class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.__points = list()

    def add_point(self, *args):
        self.__points.append([(args[0], args[1]), args[2]])

    def __check_index(self, value):
        length = len(self.__points)
        if not isinstance(value, int) or not (0 <= value < length):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__points[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__points[key][-1] = value