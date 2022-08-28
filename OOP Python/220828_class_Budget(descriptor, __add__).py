# Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите
#  два класса с именами:

# Budget - для управления семейным бюджетом;
# Item - пункт расходов бюджета.

# Объекты класса Item должны создаваться командой: it = Item(name, money)
# где name - название статьи расхода; money - сумма расходов (вещественное или целое число).

# Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с
#  переданными значениями. Также с объектами класса Item должны выполняться следующие операторы:

# s = it1 + it2 # сумма для двух статей расходов
# и в общем случае:
# s = it1 + it2 + ... + itN # сумма N статей расходов
# При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих
# объектов класса Item.

# Объекты класса Budget создаются командой: my_budget = Budget()
# А сам класс Budget должен иметь следующие методы:
# add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
# remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx 
# (индексу: отсчитывается с нуля);
# get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).



class BaseItem:
    def __set_name__(self, owenr, name):
        self.__name = f'_{owenr.__name__}__{name}'
    
    def __get__(self, instanse, owner):
        return getattr(instanse, self.__name)

    def __set__(self, instance, value):
        key = self.__name.split('_')[-1]
        if (key == 'name' and type(value) == str) or (key == 'money' and type(value) in (int, float) and value >= 0):
            setattr(instance, self.__name, value)
        else:
            raise AttributeError('Wrong values: name has to be "string" and money >= 0.')


class Item:
    name = BaseItem()
    money = BaseItem()

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @classmethod
    def __valid_types(cls, value):
        if not isinstance(value, (Item, int, float)):
            raise ArithmeticError('Operand has to be of the type "Item", "int" or "float".')
        return True

    def __add__(self, other):
        if self.__valid_types(other):
            value = other if type(other) in (int, float) else other.money
        return self.money + value

    def __radd__(self, other):
        if self.__valid_types(other):
            return self + other


class Budget:
    def __init__(self):
        self.__items = list()

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, indx):
        self.__items.pop(indx)

    def get_items(self):
        return self.__items