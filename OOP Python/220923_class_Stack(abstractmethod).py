# Oбъявите базовый класс с именем StackInterface со следующими абстрактными методами:
# def push_back(self, obj) - добавление объекта в конец стека;
# def pop_back(self) - удаление последнего объекта из стека.

# На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:
# st = Stack()
# и в каждом объекте этого класса должен формироваться локальный атрибут:
# _top - ссылка на первый объект стека (для пустого стека _top = None).

# В самом классе Stack переопределить абстрактные методы базового класса:
# def push_back(self, obj) - добавление объекта в конец стека;
# def pop_back(self) - удаление последнего объекта из стека.

# Сами объекты стека должны определяться классом StackObj и создаваться командой:
# obj = StackObj(data)
# где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически
# формироваться атрибуты:
# _data - информация, хранящаяся в объекте (строка);
# _next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).



from abc import ABC, abstractmethod

class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, obj):
        self._next = obj


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top:
            node = self._top
            while node.next:
                node = node.next
            node.next = obj
        else:
            self._top = obj

    def pop_back(self):
        if self._top:
            cur, last = self._top, self._top
            while last.next:
                cur, last = last, last.next
            cur.next = None
            if last == self._top:
                self._top = None
            return last
        return None