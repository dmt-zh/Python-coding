# Объявите класс DateString для представления дат, объекты которого создаются командой:
# date = DateString(date_string) где date_string - строка с датой в формате: "DD.MM.YYYY"
# здесь DD - день (целое число от 1 до 31);
# MM - месяц (целое число от 1 до 12);
# YYYY - год (целое число от 1 до 3000).

# Например: date = DateString("26.05.2022") или date = DateString("26.5.2022") # незначащий ноль может отсутствовать
# Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:
# DateError - класс-исключения, унаследованный от класса Exception.

# В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:
# "DD.MM.YYYY"
# (здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна формироваться строка "26.05.2022").

# Далее, в программе выполняется считывание строки из входного потока командой:
# date_string = input()

# Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:
# print(date) # date - объект класса DateString
# Если же произошло исключение, то вывести сообщение (без кавычек): "Неверный формат даты"



class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self._day, self._month, self._year = self.__get_values(date_string)

    def __get_values(self, strng):
        try:
            day, month, year = map(int, strng.split('.'))
            self.__check_values(day, month, year)
            return day, month, year
        except (ValueError, AttributeError):
            raise DateError

    @staticmethod
    def __check_values(*args):
        valid_day = 1 <= args[0] <= 31
        valid_month = 1 <= args[1] <= 12
        valid_year = 1 <= args[2] <= 3000
        if not all([valid_day, valid_month, valid_year]):
            raise AttributeError

    def __str__(self):
        return f"{self._day:02}.{self._month:02}.{self._year}"



date_string = input()

try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")