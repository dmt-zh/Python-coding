# бъявите класс GeyserClassic - фильтр для очистки воды.
# В этом классе должно быть три слота для фильтров. Каждый слот строго для своего класса фильтра:
# Mechanical - для очистки от крупных механических частиц;
# Aragon - для последующей очистки воды;
# Calcium - для обработки воды на третьем этапе.

# Объекты классов фильтров должны создаваться командами:
# filter_1 = Mechanical(дата установки)
# filter_2 = Aragon(дата установки)
# filter_3 = Calcium(дата установки)

# Во всех объектах этих классов должен формироваться локальный атрибут:
# date - дата установки фильтров (для простоты - положительное вещественное число).
# Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
# В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.

# Объекты класса GeyserClassic должны создаваться командой: g = GeyserClassic()
# А сам класс иметь атрибут:  MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого) и следующие методы:

# add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
# если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты
# класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
# remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
# get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
# water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.

# Метод water_on() должен возвращать значение True при выполнении следующих условий:
# - все три фильтра установлены в слотах;
# - все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])



import time
class GeyserClassic:
    MAX_DATE_FILTER = 100
    SLOTS = {1: ('slot_1', 'Mechanical'), 2: ('slot_2', 'Aragon'), 3: ('slot_3', 'Calcium')}

    def __init__(self):
        self.slot_1 = self.slot_2 = self.slot_3 = None

    def add_filter(self, slot_num, filter):
        slot = self.SLOTS.get(slot_num)[0]
        name = self.SLOTS.get(slot_num)[1]
        if not getattr(self, slot) and name == filter.__class__.__name__:
            setattr(self, slot, filter)

    def remove_filter(self, slot_num):
        slot = self.SLOTS.get(slot_num)[0]
        if getattr(self, slot):
            setattr(self, slot, None)

    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def water_on(self):
        filters_installed = all(list(self.get_filters()))
        if filters_installed:
            timing = time.time()
            return all(tuple(map(lambda x: 0 <= (timing - x.date) <= self.MAX_DATE_FILTER, self.get_filters())))
        return False


class BaseFilter:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Mechanical(BaseFilter):
    pass

class Aragon(BaseFilter):
    pass

class Calcium(BaseFilter):
    pass