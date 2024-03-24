# Напишите класс специализированного потока MyThread, который:
# Имеет дополнительные атрибуты target, result. Значение обоих атрибутов по умолчанию None.
# Имеет проверку указания целевой функции. В функции run() класса должна осуществляться  проверка напередачу целевой 
# функции (назначение target). Если target не назначен (остался в значении по умолчанию) - возбуждать исключение NoTargetException,
# где в качестве единственного позиционного аргумента передать имя потока. Если target назначен, присвоить атрибуту result значение,
# возвращаемое целевой функцией указанной в target.

# При выполнении целевая функция может возбуждать различные исключения, поэтому дополнительно необходимо:
# Определить функцию custom_hook, которая выводит на печать строку вида:
# name (id=ID) failed, где name - имя потока, ID - идентификатор потока (ident).

# Например:
# T3 (id=77) failed
# Указать эту функцию в качестве функции перехвата исключений.


import threading

class MyThread(threading.Thread):
    def __init__(self, target=None, result=None, name="MyThread"):
        super().__init__()
        self.target = target
        self.result = result
        self.name = name

    def run(self):
        if self.target is None:
            raise NoTargetException(self.name)
        self.result = self.target()


def custom_hook(arg):
    *_, exc_thread = arg
    print(f'{exc_thread.name} (id={exc_thread.ident}) failed')

threading.excepthook = custom_hook
