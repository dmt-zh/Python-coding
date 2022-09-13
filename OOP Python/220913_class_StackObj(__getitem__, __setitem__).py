# Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке
# до последнего.

# Для этого в программе объявлялись два класса:
# StackObj - для описания объектов стека;
# Stack - для управления стек-подобной структурой.

# И, далее, объекты класса StackObj следовало создавать командой:
# obj = StackObj(data)
# где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен
# иметь следующие локальные атрибуты:
# data - ссылка на строку с данными, указанными при создании объекта;
# next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

# Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта стек-подобной структуры

# В каждом объекте класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый объект стека (если стек пуст, то top = None).

# А в самом классе Stack следующие методы:
# push(self, obj) - добавление объекта класса StackObj в конец стека;
# pop(self) - извлечение последнего объекта с его удалением из стека;

# Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:
# obj_top = st[0] # получение первого объекта
# obj = st[4] # получение 5-го объекта стека
# st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый

# Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться
# исключение командой: raise IndexError('неверный индекс')
# Пример использования классов Stack и StackObj (эти строчки в программе не писать):

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
# res = st[3] # исключение IndexError




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

    def push(self, obj):
        if self.__size == 0:
            self.top = obj
        else:
            node = self[self.__size - 1]
            node.next = obj
        self.__size += 1

    def pop(self):
        idx = self.__size
        if idx == 0:
            return
        node = self[idx - 2] if idx > 2 else self[idx - 1]
        last = node.next
        node.next = None
        self.__size -= 1
        return last

    def __check_index(self, value):
        if type(value) != int or not 0 <= value < self.__size:
            raise IndexError('неверный индекс')

    def __getitem__(self, idx):
        self.__check_index(idx)
        cnt, node = 0, self.top
        while cnt != idx:
            node = node.next
            cnt += 1
        return node

    def __setitem__(self, idx, obj):
        self.__check_index(idx)
        node = self.top
        if idx == 0 and node:
            node = self.top
            if node.next:
                self.top = obj
                obj.next = node.next
            self.top = obj
        else:
            prev_node = self[idx - 1] if idx - 1 >= 0 else None
            next_node = self[idx + 1] if idx + 1 < self.__size else None
            if prev_node and next_node:
                prev_node.next = obj
                obj.next = next_node
            prev_node.next = obj