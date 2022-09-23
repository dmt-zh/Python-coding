# Bначале нужно объявить базовый класс Validator, в котором должен отсутствовать инициализатор
# (магический метод __init__) и объявлен метод со следующей сигнатурой:
# def _is_valid(self, data): ...

# По идее, этот метод возвращает булево значение True, если данные (data) корректны с точки зрения валидатора,
# и False - в противном случае. Но в базовом классе Validator он должен генерировать исключение командой:
# raise NotImplementedError('в классе не переопределен метод _is_valid')

# Затем, нужно объявить дочерний класс FloatValidator для валидации вещественных чисел. Объекты этого класса
# создаются командой: float_validator = FloatValidator(min_value, max_value)
# где min_value - минимально допустимое значение; max_value - максимально допустимое значение.

# Пользоваться объектами класса FloatValidator предполагается следующим образом:
# res = float_validator(value)
# где value - проверяемое значение (должно быть вещественным и находиться в диапазоне [min_value; max_value]).
# Данный валидатор должен возвращать True, если значение value проходит проверку, и False - в противном случае.




class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value=0.0, max_value=100.0):
        self.__min_value = min_value
        self.__max_value = max_value

    def _is_valid(self, data):
        return type(data) == float and self.__min_value <= data <= self.__max_value

    def __call__(self, value, *args, **kwargs):
        return self._is_valid(value)