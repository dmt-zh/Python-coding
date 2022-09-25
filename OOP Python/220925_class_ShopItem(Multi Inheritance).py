# В программе объявлены два класса:

# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id


# class Book(ShopItem):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year

# Затем, создается объект класса Book (книга) и отображается в консоль:
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)

# В результате, на экране увидим что то вроде:
# <__main__.Book object at 0x0000015FBA4B3D00>

# Но нам требуется, чтобы здесь отображались локальные атрибуты объекта с их значениями в формате:
# <атрибут_1>: <значение_1>
# <атрибут_2>: <значение_2>
# ...
# <атрибут_N>: <значение_N>

# Для этого вам дают задание разработать два класса:
# ShopGenericView - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);
# ShopUserView - для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних
# классов (не только Book).




class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        return '\n'.join((f'{k}: {v}' for k, v in self.__dict__.items()))


class ShopUserView:
    def __str__(self):
        attrs = (f'{k}: {v}' for k, v in self.__dict__.items() if k != '_id')
        return '\n'.join(attrs)


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


class Item(Book, ShopGenericView):
    pass



book = Item("Python ООП", "Балакирев", 2022)
print(book)