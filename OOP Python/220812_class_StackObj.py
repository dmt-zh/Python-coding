# Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
# когда один объект ссылается на следующий и так по цепочке до последнего элемента.
# Для этого объявите в программе два класса:

# StackObj - для описания объектов односвязного списка;
# Stack - для управления односвязным списком.

# Объекты класса StackObj предполагается создавать командой:
# obj = StackObj(данные)
# Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные
# приватные атрибуты:
# __data - ссылка на строку с данными, указанными при создании объекта;
# __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

# Также в классе StackObj должны быть объявлены объекты-свойства:
# next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.

# При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None.
# Если проверка не проходит, то __next остается без изменений.

# Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта односвязного списка
# В объектах класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

# А в самом классе Stack следующие методы:
# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого
# объекта в порядке их добавления, или пустой список, если объектов нет).


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

    def push(self, obj):
        if self.top:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj
        else:
            self.top = obj

    def pop(self):
        curr_node = self.top
        prev_node = curr_node
        while curr_node.next:
            prev_node, curr_node = curr_node, curr_node.next
        prev_node.next = None
        if self.top.next is None:
            self.top = None
        return curr_node

    def get_data(self):
        lst = []
        node = self.top
        while node:
            lst.append(node.data)
            node = node.next
        return lst



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.pop().data)
res = st.get_data()
print(res)