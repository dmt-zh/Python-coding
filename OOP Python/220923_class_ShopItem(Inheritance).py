# Вам необходимо объявить базовый класс ShopInterface с абстрактным методом:
# def get_id(self): ...

# В самом методе должно генерироваться исключение командой:
# raise NotImplementedError('в классе не переопределен метод get_id')
# Инициализатор в классе ShopInterface прописывать не нужно.
#
# Далее объявите дочерний класс ShopItem (от базового класса ShopInterface), объекты которого создаются командой:
# item = ShopItem(name, weight, price)
# где name - название товара (строка);
# weight - вес товара (любое положительное число);
# price - цена товара (любое положительное число).

# В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name, _weight, _price
# и соответствующими значениями. Также в объектах класса ShopItem должен автоматически формироваться локальный
# приватный атрибут __id с уникальным (для каждого товара) целым значением.

# В классе ShopItem необходимо переопределить метод get_id() базового класса так, чтобы он (метод) возвращал
# значение атрибута __id.




class ShopInterface:

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self._name = self._valid_attr(name, str)
        self._weight = self._valid_attr(weight, (int, float), positive=True)
        self._price = self._valid_attr(price, (int, float), positive=True)
        self.__id = abs(hash((name, weight, price)))

    @staticmethod
    def _valid_attr(attr, attr_type, positive=False):
        valid_type = isinstance(attr, attr_type)
        gt_zero = attr > 0 if positive else True
        if not (valid_type and gt_zero):
            raise AttributeError('Неверное значение атрибута: имя -> строка; вес и цена -> положительное цисло.')
        return attr

    def get_id(self):
        return self.__id