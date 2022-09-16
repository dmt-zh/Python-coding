# Объявите в программе класс Person, объекты которого создаются командой:
# p = Person(fio, job, old, salary, year_job)
# где fio - ФИО сотрудника (строка);
# job - наименование должности (строка);
# old - возраст (целое число); 
# salary - зарплата (число: целое или вещественное);
# year_job - непрерывный стаж на указанном месте работы (целое число).

# В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами:
# fio, job, old, salary, year_job и соответствующими значениями.

# Также с объектами класса Person должны поддерживаться следующие команды:
# data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary,
# year_job и начинается с нуля)

# p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
#     print(v)

# При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4].
# Иначе, генерировать исключение командой: raise IndexError('неверный индекс')



class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__info = {k: v for k, v in zip(range(5), [fio, job, old, salary, year_job])}
        self.__start = -1

    @staticmethod
    def __check_index(idx):
        if type(idx) != int or not 0 <= idx < 5:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__info.get(item)

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__info.update({key: value})

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start + 1 < 5:
            self.__start += 1
            return self.__info.get(self.__start)
        else:
            raise StopIteration