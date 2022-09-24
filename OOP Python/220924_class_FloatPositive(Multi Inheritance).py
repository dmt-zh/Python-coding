# Определите в программе классы в соответствии с их иерархией:
# Digit, Integer, Float, Positive, Negative

# Каждый объект этих классов должен создаваться однотипной командой вида:
# obj = Имя_класса(value)
# где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:
# - в классе Digit: value - любое число;
# - в классе Integer: value - целое число;
# - в классе Float: value - вещественное число;
# - в классе Positive: value - положительное число;
# - в классе Negative: value - отрицательное число.

# Если проверка не проходит, то генерируется исключение командой:
# raise TypeError('значение не соответствует типу объекта')

# После этого объявите следующие дочерние классы:
# PrimeNumber - простые числа; наследуется от классов Integer и Positive;
# FloatPositive - наследуется от классов Float и Positive.

# Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными
# допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
# lst_positive - все объекты, относящиеся к классу Positive;
# lst_float - все объекты, относящиеся к классу Float.




class Digit:
    def __new__(cls, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass



digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5),
          FloatPositive(9.2), FloatPositive(6.5), FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
