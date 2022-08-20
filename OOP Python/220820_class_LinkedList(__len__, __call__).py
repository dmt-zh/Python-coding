# Объявите класс LinkedList (связный список).
# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:
# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
# локальные атрибуты:
# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

# В свою очередь, объекты класса LinkedList должны создаваться командой: linked_lst = LinkedList()
# и содержать локальные атрибуты:
# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

# А сам класс содержать следующие методы:
# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

# Также с объектами класса LinkedList должны поддерживаться следующие операции:
# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx
# (в связном списке).

# Пример использования классов (эти строчки в программе писать не нужно):
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev



class ObjList:
    def __init__(self, data=None):
        self.__next = self.__prev = None
        self.data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, obj):
        self.__next = obj

    @property
    def prev_node(self):
        return self.__prev

    @prev_node.setter
    def prev_node(self, obj):
        self.__prev = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None

    def __len__(self):
        node = self.head
        cnt = 0
        while node:
            node = node.next_node
            cnt += 1
        return cnt

    def __get_obj_by_index(self, indx):
        node = self.head
        acc = 0
        while node and acc < indx:
            node = node.next_node
            acc += 1
        return node

    def add_obj(self, obj):
        if self.tail:
            self.tail.next_node = obj
        obj.prev_node = self.tail
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)

        if obj is None:
            return None

        prev_, next_ = obj.prev_node, obj.next_node
        if prev_:
            prev_.next_node = next_
        if next_:
            next_.prev_node = prev_

        if self.head == obj:
            self.head = next_
        if self.tail == obj:
            self.tail = prev_