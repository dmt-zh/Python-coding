# Объявите класс Dimensions (габариты) с атрибутами:
# MIN_DIMENSION = 10
# MAX_DIMENSION = 10000

# Каждый объект класса Dimensions должен создаваться командой
# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого
# класса.

# Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены 
# объекты-свойства (property) с именами: a, b, c. Причем, в момент присваивания нового значения 
# должна выполняться проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION]. 
# Если число не попадает, то оно игнорируется и существующее значение не меняется.

# С объектами класса Dimensions должны выполняться следующие операторы сравнения:
# dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
# dim1 > dim2    # True, если объем dim1 больше объема dim2
# dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
# dim1 < dim2    # True, если объем dim1 меньше объема dim2

# Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:
# item = ShopItem(name, price, dim)
# где name - название товара (строка); price - цена товара (целое или вещественное число);
#  dim - габариты товара (объект класса Dimensions).

# В каждом объекте класса ShopItem должны создаваться локальные атрибуты:
# name - название товара;
# price - цена товара;
# dim - габариты товара (объект класса Dimensions).

# Создайте список с именем lst_shop из четырех товаров со следующими данными:
# - кеды; 1024; (40, 30, 120)
# - зонт; 500.24; (10, 20, 50)
# - холодильник; 40000; (2000, 600, 500)
# - табуретка; 2000.99; (500, 200, 200)

# Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров
#  списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр key для 
# настройки сортировки. Прежний список lst_shop должен оставаться без изменений.




class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = 0
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __valid_range(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @classmethod
    def __valid_types(cls, obj):
        return isinstance(obj, Dimensions)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__valid_range(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__valid_range(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__valid_range(value):
            self.__c = value

    def get_volume(self):
        return self.a * self.b * self.c

    def __gt__(self, other):
        if self.__valid_types(other):
            return self.get_volume() > other.get_volume()

    def __ge__(self, other):
        if self.__valid_types(other):
            return self.get_volume() >= other.get_volume()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim



lst_shop = [
    ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
    ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
    ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
    ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim.get_volume())