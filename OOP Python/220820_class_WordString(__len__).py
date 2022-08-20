#  Объявите класс WordString, объекты которого создаются командами:
# w1 = WordString()
# где string - передаваемая строка. Например: words = WordString("Курс по Python ООП")

# Реализовать следующий функционал для объектов этого класса:
# len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
# words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).

# Также в классе WordString реализовать объект-свойство (property):
# string - для передачи и считывания строки.

# Пример пользования классом WordString (эти строчки в программе писать не нужно):
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")



class WordString:
    def __init__(self, strng):
        self.string = strng
        self.__lst = self.__strng.split()

    def __call__(self, indx, *args, **kwargs):
        return self.__lst[indx]

    @property
    def string(self):
        return self.__strng

    @string.setter
    def string(self, value):
        if isinstance(value, str):
            self.__strng = value

    def __len__(self):
        return len(self.__lst)