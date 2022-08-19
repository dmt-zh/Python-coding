# Объявите класс-декоратор InputDigits для декорирования стандартной функции input так,
# чтобы при вводе строки из целых чисел, записанных через пробел, например:
# "12 -5 10 83"

# на выходе возвращался список из целых чисел:
# [12, -5, 10, 83]

# Назовите декорированную функцию input_dg и вызовите ее командой:
# res = input_dg()



class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        strng = self.func().split()
        lst = filter(lambda x: (x.startswith('-') and x[1:].isdigit()) or x.isdigit(), strng)
        return list(map(int, lst))


input_dg = InputDigits(input)
res = input_dg()