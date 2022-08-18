# Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:
# rnd = RandomPassword(psw_chars, min_length, max_length)
# где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина
# генерируемых паролей.

# Непосредственная генерация одного пароля должна выполняться командой:
# psw = rnd()
# где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.

# С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword,
# созданного с параметрами:
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"



from random import choice, randint

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.chars = psw_chars
        self.min_ = min_length
        self.max_ = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(choice(self.chars) for _ in range(randint(self.min_, self.max_)))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]
