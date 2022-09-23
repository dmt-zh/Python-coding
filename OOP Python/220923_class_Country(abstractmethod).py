# Oбъявите базовый класс с именем CountryInterface со следующими абстрактными методами и свойствами:
# name - абстрактное свойство (property), название страны (строка);
# population - абстрактное свойство (property), численность населения (целое положительное число);
# square - абстрактное свойство (property), площадь страны (положительное число);
# get_info() - абстрактный метод для получения сводной информации о стране.

# На основе класса CountryInterface объявите дочерний класс Country, объекты которого создаются командой:
# country = Country(name, population, square)

# В самом классе Country должны быть переопределены следующие свойства и методы базового класса:
# name - свойство (property) для считывания названия страны (строка);
# population - свойство (property) для записи и считывания численности населения (целое положительное число);
# square - свойство (property) для записи и считывания площади страны (положительное число);
# get_info() - метод для получения сводной информации о стране в виде строки:
# "<название>: <площадь>, <численность населения>"




from abc import ABC, abstractmethod

class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @staticmethod
    def __attr_is_valid(attr, attr_type, positive=False):
        valid = isinstance(attr, attr_type)
        gt_zero = True
        if positive:
            gt_zero = attr > 0 if valid else False
        if not (valid and gt_zero):
            raise AttributeError('неверное значение присваемого атрибута.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__attr_is_valid(name, str)
        self.__name = name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, data):
        self.__attr_is_valid(data, (float, int), positive=True)
        self.__population = data

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, data):
        self.__attr_is_valid(data, (float, int), positive=True)
        self.__square = data

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"