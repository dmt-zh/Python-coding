# Допишите недостающий код класса. Класс всего-лишь запускает функцию обработки (функция принимает один единственный числовой аргумент),
# которая в результате своей работы возвращает один единственный результат - число (тип float, double).

# В тестирующей системе будут запущенны несколько экземпляров класса. Главный процесс вычислит сумму результатов работы дочерних процессов,
# обращаясь к атрибуту result.value.

# Если бы функция обработки для следующих входных параметров возвращала результаты:
# 1 -> 10.00009
# 87 -> -999.99001
# -3 -> 1000000.001
# то общая сумма результатов должна быть равна 999010.01108000...



import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, target = None, args = None):
        super().__init__()
        self.target = target
        self.args = args
        self.result = multiprocessing.Value('d', 0)

    def run(self):
        result = self.target(*self.args)
        self.result.value = result