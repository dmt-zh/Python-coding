# В программе объявлены два класса:

# class Student:
#     def __init__(self, fio, group):
#         self._fio = fio  # ФИО студента (строка)
#         self._group = group # группа (строка)
#         self._lect_marks = []  # оценки за лекции
#         self._house_marks = []  # оценки за домашние задания
#
#     def add_lect_marks(self, mark):
#         self._lect_marks.append(mark)
#
#     def add_house_marks(self, mark):
#         self._house_marks.append(mark)
#
#     def __str__(self):
#         return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


# class Mentor:
#     def __init__(self, fio, subject):
#         self._fio = fio
#         self._subject = subject

# Первый класс описывает студентов, а второй - менторов. Вам поручается на основе базового класса Mentor
# разработать еще два дочерних класса:
# Lector - для описания лекторов;
# Reviewer - для описания экспертов.

# Объекты этих классов должны создаваться командами:
# lector = Lector(fio, subject)
# reviewer = Reviewer(fio, subject)
# где fio - ФИО (строка); subject - предмет (строка).
# Инициализации этих параметров (fio, subject) должна выполняться базовым классом Mentor.
#
# В самих классах Lector и Reviewer необходимо объявить метод:
# def set_mark(self, student, mark): ...
# для простановки оценки (mark) студенту (student). Причем, в классе Lector оценки добавляются в список _lect_marks
# объекта класса Student, а в классе Reviewer - в список _house_marks. Используйте для этого методы add_lect_marks()
# и add_house_marks() класса Student.

# Также в классах Lector и Reviewer должен быть переопределен магический метод: __str__() для формирования
# следующей информации об объектах:
# - для объектов класса Lector: Лектор <ФИО>: предмет <предмет>
# - для объектов класса Reviewer: Эксперт <ФИО>: предмет <предмет>



class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []
        self._house_marks = []

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    _ROLE = 'Mentor'

    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def set_mark(self, *args, **kwargs):
        name = self.__class__.__name__
        raise NotImplementedError(f'В дочернем классе {name} не реализован метод set_mark')

    def __str__(self):
        return f'{self._ROLE} {self._fio}: предмет {self._subject}'


class Lector(Mentor):
    _ROLE = 'Лектор'

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    _ROLE = 'Эксперт'

    def set_mark(self, student, mark):
        student.add_house_marks(mark)