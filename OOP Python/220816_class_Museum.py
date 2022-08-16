# Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum,
# объекты которого формируются командой: mus = Museum(название музея)
# В объектах этого класса должны формироваться следующие локальные атрибуты:
# name - название музея (строка);
# exhibits - список экспонатов (изначально пустой список).

# Сам класс Museum должен иметь методы:
# add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
# remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
# get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).

# Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:
# Picture - для картин;
# Mummies - для мумий;
# Papyri - для папирусов.

# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
# m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
# pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
# Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:
# "Описание экспоната {name}: {descr}"



class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = list()

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        item = self.exhibits[indx]
        return f"Описание экспоната {item.name}: {item.descr}"


class BaseExhibit:
    set_attr = None
    def __init__(self, name, change_attr, descr):
        self.name = name
        self.attr = change_attr
        self.descr = descr

    def __setattr__(self, key, value):
        if key == 'attr':
            key = self.set_attr
        super().__setattr__(key, value)


class Picture(BaseExhibit):
    set_attr = 'author'
    pass

class Mummies(BaseExhibit):
    set_attr = 'location'
    pass


class Papyri(BaseExhibit):
    set_attr = 'date'
