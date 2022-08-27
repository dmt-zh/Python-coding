# Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:
# Lib - для представления библиотеки в целом;
# Book - для описания отдельной книги.

# Объекты класса Book должны создаваться командой:
# book = Book(title, author, year)
# где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

# Объекты класса Lib создаются командой:
# lib = Lib()
# Каждый объект должен содержать локальный публичный атрибут:
# book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

# Также объекты класса Lib должны работать со следующими операторами:
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book
# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx

# При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
# Также с объектами класса Lib должна работать функция:
# n = len(lib) # n - число книг
# которая возвращает число книг в библиотеке.



class BookInfo:
    def __set_name__(self, owner, name):
        self.__name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.__name)

    def __set__(self, instance, value):
        key = self.__name.split('_')[-1]
        if (key == 'year' and type(value) == int and value > 0) or (key in ('title', 'author') and type(value) == str):
            setattr(instance, self.__name, value)
        else:
            raise AttributeError('Incorrect name or value: year > 0, [title, author] -> string')


class Book:
    title = BookInfo()
    author = BookInfo
    year = BookInfo()

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = list()

    def __add__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError('Operand has to be Book object.')
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            if other in self.book_list:
                self.book_list.remove(other)
        elif type(other) == int:
            if other <= len(self):
                self.book_list.pop(other)
        else:
            raise ArithmeticError('Operand has to be "Book" object or type "int".')
        return self

    def __len__(self):
        return len(self.book_list)