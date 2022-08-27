# Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj
# (когда один объект ссылается на следующий и так далее):
# Давайте снова создадим такую структуру данных. Для этого объявим два класса:

# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.

# Объекты класса StackObj должны создаваться командой: obj = StackObj(data)  где data - строка с некоторыми данными.

# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

# Объекты класса Stack создаются командой:
# st = Stack()mи каждый из них должен содержать локальный атрибут:
# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

# Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.

# Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):
# добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj

# добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка
# (каждый элемент списка для очередного добавляемого объекта).



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

    def push_back(self, obj):
        if self.top:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj
        else:
            self.top = obj

    def pop_back(self):
        curr_node = self.top
        prev_node = curr_node
        while curr_node.next:
            prev_node, curr_node = curr_node, curr_node.next
        prev_node.next = None
        if self.top.next is None:
            self.top = None
        return curr_node

    def __add__(self, other):
        if not isinstance(other, StackObj):
            raise ArithmeticError('Operand has to be StackObj.')
        self.push_back(other)
        return self

    def __mul__(self, other):
        if not type(other) == list:
            raise ArithmeticError('Operand has to be type "list" containing elements with type "string".')
        if len(other) > 0:
            for obj in map(StackObj, other):
                self.push_back(obj)
        return self

    def get_data(self):
        lst = []
        node = self.top
        while node:
            lst.append(node.data)
            node = node.next
        return lst