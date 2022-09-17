# Нужно объявить классы:
# Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.

# В классе Stack должны быть методы:
# push_back(obj) - для добавления нового объекта obj в конец стека;
# push_front(obj) - для добавления нового объекта obj в начало стека.

# В каждом объекте класса Stack должен быть публичный атрибут:
# top - ссылка на первый объект стека (при пустом стеке top = None).

# Объекты класса StackObj создаются командой:
# obj = StackObj(data)
# где data - данные, хранящиеся в объекте стека (строка).

# Также в каждом объекте класса StackObj должны быть публичные атрибуты:
# data - ссылка на данные объекта;
# next - ссылка на следующий объект стека (если его нет, то next = None).

# Наконец, с объектами класса Stack должны выполняться следующие команды:
# st = Stack()
# st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
# data = st[indx]  # получение данных из объекта стека по индексу
# n = len(st) # получение общего числа объектов стека

# for obj in st: # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль

# При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1,
# где N - число объектов в стеке. Иначе, генерировать исключение командой:
# raise IndexError('неверный индекс')


class StackObj:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        self.__size = 0

    def push_back(self, obj):
        if self.__size == 0:
            self.top = obj
        else:
            node = self.__get_node(self.__size - 1, data=False)
            node.next = obj
        self.__size += 1

    def push_front(self, obj):
        if self.__size == 0:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self.__size += 1

    def pop(self):
        idx = self.__size
        if idx == 0:
            return
        node = self.__get_node(idx - 2, data=False) if idx > 2 else self.__get_node(idx - 1, data=False)
        last = node.next
        node.next = None
        self.__size -= 1
        return last

    def __len__(self):
        return self.__size

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def __check_index(self, value):
        if type(value) != int or not 0 <= value < self.__size:
            raise IndexError('неверный индекс')

    def __get_node(self, idx, data=True):
        self.__check_index(idx)
        iterator = iter(self)
        for _ in range(idx):
            next(iterator)
        node = next(iterator)
        if data:
            return node.data
        return node

    def __getitem__(self, idx):
        return self.__get_node(idx)

    def __setitem__(self, idx, value):
        node = self.__get_node(idx, data=False)
        node.data = str(value)