# Объявите класс с именем Book (книга), объекты которого создаются командой:
# book = Book(title, author, pages)
# где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).

# Также при выводе информации об объекте на экран командой: print(book) должна отображаться строчка в формате:
# "Книга: {title}; {author}; {pages}"

# Например:
# "Книга: Муму; Тургенев; 123"

# Прочитайте из входного потока строки с информацией по книге командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# (строки идут в порядке: title, author, pages). Создайте объект класса Book и выведите его строковое представление в консоль.



import sys

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __str__(self):
        return f"Книга: {self.__title}; {self.__author}; {self.__pages}"

lst_in = list(map(str.strip, sys.stdin.readlines()))
b = Book(*lst_in)
print(b)