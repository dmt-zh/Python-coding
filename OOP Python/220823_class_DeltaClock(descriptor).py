# Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:
# dt = DeltaClock(clock1, clock2) где clock1, clock2 - объекты другого класса Clock для хранения текущего времени.

# Эти объекты должны создаваться командой:
# clock = Clock(hours, minutes, seconds) где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

# В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):
# get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

# После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
# str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

# Если разность получается отрицательной, то разницу времен считать нулевой.



class BaseClock:
    def __set_name__(self, owner, name):
        self.__name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)

    def __set__(self, instance, value):
        if not isinstance(value, int) and value < 0:
            raise AttributeError('Значение должно быть целым неотрицаттельным числом')
        setattr(instance, self.__name, value)


class Clock:
    hours = BaseClock()
    minutes = BaseClock()
    seconds = BaseClock()

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock_1, clock_2):
        self.__clock_1 = clock_1
        self.__clock_2 = clock_2

    def __len__(self):
        delta = self.__clock_1.get_time() - self.__clock_2.get_time()
        return delta if delta >= 0 else 0

    def __str__(self):
        delta = self.__len__()
        h = delta // 3600
        m = delta % 3600 // 60
        s = delta % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'