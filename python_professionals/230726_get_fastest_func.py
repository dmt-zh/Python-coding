# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление
# значения при вызове с аргументом arg наименьшее количество времени.


import time
from typing import Any, Callable, Sequence

def get_the_fastest_func(funcs: Sequence[Callable], arg: Any) -> Callable:
    min_time = float('INF')
    best_func = None
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        curr_time = end_time - start_time
        if curr_time < min_time:
            min_time = curr_time
            best_func = func
    return best_func