# Объявите в программе класс Cart (корзина), объекты которого создаются командой:
# cart = Cart()

# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки.
# Изначально этот список должен быть пустым.
# В классе Cart объявить методы:
# add(self, gd) - добавление в корзину товара, представленного объектом gd;
# remove(self, indx) - удаление из корзины товара по индексу indx;
# get_list(self) - получение из корзины товаров в виде списка из строк:
# ['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',
# ...
# '<наименовние_N>: <цена_N>']

# Объявите в программе следующие классы для описания товаров:
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.

# Объекты этих классов должны создаваться командой:
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;
# price - цена.

# Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook)
# и одну кружку (Cup). Названия и цены придумайте сами.


class Cart:
    def __init__(self):
        self.goods = list()

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return list(map(lambda x: f'{x.name}: {x.price}', self.goods))


class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Goods):
    pass

class TV(Goods):
    pass

class Notebook(Goods):
    pass

class Cup(Goods):
    pass


cart = Cart()

mock_goods = (
    TV('LG TV', 23000),
    TV('Samsung TV', 122300),
    Table('IKEA table', 3000),
    Notebook('MacBook', 289000),
    Notebook('MateBook', 102300),
    Cup('Coffee cup', 230),
)

for gd in mock_goods:
    cart.add(gd)

cart.get_list()