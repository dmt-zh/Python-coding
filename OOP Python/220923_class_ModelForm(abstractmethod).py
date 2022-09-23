# Oбъявите базовый класс Model (модель), в котором нужно объявить один абстрактный метод с сигнатурой:
# def get_pk(self): ...
# и один обычный метод:
# def get_info(self): ...
#  который бы возвращал строку "Базовый класс Model".

# На основе класса Model объявите дочерний класс ModelForm, объекты которого создаются командой:
# form = ModelForm(login, password)
# где login - заголовок перед полем ввода логина (строка); password - заголовок перед полем ввода пароля (строка).
# В каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password,
# а также автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта
# класса ModelForm.

# В классе ModelForm переопределите метод:
# def get_pk(self): ...
# который должен возвращать значение атрибута _id.




from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = abs(hash((login, password)))

    def get_pk(self):
        return self._id