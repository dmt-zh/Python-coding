# Создайте класс Book, в котором будут атрибуты name и author, со значениями из input.
# Затем выведите значения. Input и Output должны быть в следующем формате:

# Sample Input:
# Преступление и наказание
# Федор Михайлович Достоевский
# Страх и Трепет
# Сёрен Кьеркегор
# Голова профессора Доуэля
# Александр Романович Беляев

# Sample Output:
# Преступление и наказание - Федор Михайлович Достоевский
# Страх и Трепет - Сёрен Кьеркегор
# Голова профессора Доуэля - Александр Романович Беляев

import sys

class Book:
    all_books = []
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.all_books.append(self)

    def __str__(self):
        return f'{self.title} - {self.author}'

ins = [line.rstrip() for line in sys.stdin]

for book in zip(ins[::2], ins[1::2]):
    print(Book(*book))