# В программе вводятся в одну строчку через пробел некоторые данные, например:
# "1 -5.6 2 abc 0 False 22.5 hello world"

# Эти данные разбиваются по пробелу и представляются в виде списка строк: lst_in = input().split()
# Ваша задача посчитать сумму всех целочисленных значений, присутствующих в списке lst_in. Результат
# (сумму) вывести на экран.



import re

class IntParser:
    def __init__(self, s):
        self.__data = s

    def pars_int(self):
        return tuple(map(int, re.findall(r'(?<!\.|0)-\d+(?!\.)\b|\b(?<!\.|0)(?:[1-9]\d*)(?!\.)\b', self.__data)))

    def int_sum(self):
        return sum(self.pars_int())



parser = IntParser(input())
print(parser.int_sum())
