# Объявите в программе класс FloatValidator, объекты которого создаются командой:
# fv = FloatValidator(min_value, max_value)
# где min_value, max_value - минимальное и максимальное допустимое значение (диапазон [min_value; max_value]).

# Объекты этого класса предполагается использовать следующим образом: fv(value)
# где value - проверяемое значение. Если value не вещественное число или не принадлежит
# диапазону [min_value; max_value], то генерируется исключение командой:
# raise ValueError('значение не прошло валидацию')

# По аналогии, объявите класс IntegerValidator, объекты которого создаются командой:
# iv = IntegerValidator(min_value, max_value) и используются командой: iv(value)
# Здесь также генерируется исключение: raise ValueError('значение не прошло валидацию')
# если value не целое число или не принадлежит диапазону [min_value; max_value].

# После этого объявите функцию с сигнатурой:
# def is_valid(lst, validators): ...

# где lst - список из данных; validators - список из объектов-валидаторов (объектов классов FloatValidator
# и IntegerValidator). Эта функция должна отбирать из списка все значения, которые прошли хотя бы по
# одному валидатору. И возвращать новый список с элементами, прошедшими проверку.




class NumbersValidator:
    _valid_types = (int, float)

    def __init__(self, min_val, max_val):
        self._min_val = min_val
        self._max_val = max_val

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('передаваемые аргументы должны быть числами')
        object.__setattr__(self, key, value)

    def __check_value(self, value):
        valid_type = type(value) in self._valid_types
        value_in_range = self._min_val <= value <= self._max_val if valid_type else False
        if not (valid_type and value_in_range):
            raise ValueError('значение не прошло валидацию')

    def __call__(self, value, *args, **kwargs):
        self.__check_value(value)
        return value


class FloatValidator(NumbersValidator):
    _valid_types = (float,)


class IntegerValidator(NumbersValidator):
    _valid_types = (int,)



def is_valid(lst, validators):
    def apply_validatar(value):
        for checker in validators:
            try:
                return checker(value)
            except:
                continue
        return False

    return list(filter(apply_validatar, lst))


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]