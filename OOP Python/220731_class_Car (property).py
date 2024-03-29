# Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи и
# считывания информации о модели автомобиля из локальной приватной переменной __model.
# Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны быть реализованы проверки:
# - модель автомобиля - это строка;
# - длина строки модели должна быть в диапазоне [2; 100].

# Если проверка не проходит, то локальное свойство __model остается без изменений.
# Объекты класса Car предполагается создавать командой:
# car = Car()
# и далее работа с объектом-свойством, например: car.model = "Toyota"



class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, name):
        if self.__name_is_valid(name):
            self.__model = name

    @staticmethod
    def __name_is_valid(name):
        return type(name) == str and 2 <= len(name) <= 100