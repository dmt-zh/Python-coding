# Объявите в программе базовый класс с именем IteratorAttrs для перебора всех локальных атрибутов
# объектов класса. Объявите дочерний класс SmartPhone, объекты которого создаются командой:
# phone = SmartPhone(model, size, memory)
# где model - модель смартфона (строка);
# size - габариты (ширина, длина) в виде кортежа двух чисел;
# memory - размер ОЗУ (памяти), как целое число.

# В каждом объекте класса SmartPhone должны создаваться соответствующие локальные атрибуты: model, size, memory.
# Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone должен выполняться
# оператор for:

# for attr, value in phone:
#     print(attr, value)




class IteratorAttrs:
    def __iter__(self):
        for attr in self.__dict__.items():
            yield attr


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory