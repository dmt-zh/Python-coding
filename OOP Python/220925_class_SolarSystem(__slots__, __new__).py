# Объявите класс Planet (планета), объекты которого создаются командой:
# p = Planet(name, diametr, period_solar, period)
# где name - наименование планеты;
# diametr - диаметр планеты (любое положительное число);
# period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число);
# period - период обращения планеты вокруг своей оси (любое положительное число).

# В каждом объекте класса Planet должны формироваться локальные атрибуты с именами: _name, _diametr,
# _period_solar, _period и соответствующими значениями.

# Затем, объявите класс с именем SolarSystem (солнечная система). В объектах этого класса должны быть допустимы,
# следующие локальные атрибуты (ограничение задается через коллекцию __slots__):

# _mercury - ссылка на планету Меркурий (объект класса Planet);
# _venus - ссылка на планету Венера (объект класса Planet);
# _earth - ссылка на планету Земля (объект класса Planet);
# _mars - ссылка на планету Марс (объект класса Planet);
# _jupiter - ссылка на планету Юпитер (объект класса Planet);
# _saturn - ссылка на планету Сатурн (объект класса Planet);
# _uranus - ссылка на планету Уран (объект класса Planet);
# _neptune - ссылка на планету Нептун (объект класса Planet).

# Объект класса SolarSystem должен создаваться командой: s_system = SolarSystem() и быть только один (одновременно
# в программе два и более объектов класса SolarSystem недопустимо). Используйте для этого паттерн Singleton.

# В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные атрибуты и ссылаться
# на соответствующие объекты класса Planet со следующими данными по планетам:

# 'Меркурий', 4878, 87.97, 1407.5
# 'Венера', 12104, 224.7, 5832.45
# 'Земля', 12756, 365.3, 23.93
# 'Марс', 6794, 687, 24.62
# 'Юпитер', 142800, 4330, 9.9
# 'Сатурн', 120660, 10753, 10.63
# 'Уран', 51118, 30665, 17.2
# 'Нептун', 49528, 60150, 16.1

# Создайте в программе объект s_system класса SolarSystem.



class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = self.__valid_attr(name, True)
        self._diametr = self.__valid_attr(diametr)
        self._period_solar = self.__valid_attr(period_solar)
        self._period = self.__valid_attr(period)

    @staticmethod
    def __valid_attr(attr, string=False):
        valid_name = isinstance(attr, str) if string else True
        valid_nambers = isinstance(attr, (int, float)) if not string else True
        above_zero = attr > 0 if valid_nambers and not string else True
        if not (valid_name and valid_nambers and above_zero):
            raise AttributeError(f'Недопустимое значение атрибута {attr}')
        return attr


class SolarSystem:
    __exist = None
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    def __new__(cls, *args, **kwargs):
        if cls.__exist is None:
            cls.__instance = super().__new__(cls)
        return cls.__exist

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)



s_system = SolarSystem()