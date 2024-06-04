# Необходимо запустить на исполнение расчетную задачу task в пуле процессов. Известно, что функция task принимает один аргумент и может
# выполняться значительное время. Необходимо решение, позволяющее ограничить время ожидания работы функции в пуле процессов. Оформите ваш
# код в виде функции main(), которая принимает объект задачи, итератор аргументов для задач task и значение таймаута.

# Допишите код так, чтобы функция возвращала список результатов. Порядок в списке должен соответствовать порядку итератора аргументов.
# Если пул потоков выполняется дольше чем указанный таймаут - то вместо результата в списке должно быть строковое значение "TimeoutError".

# Функция task и iterable заданы в тестирующей системе. Гарантируется, что во время выполнения функции task не будет исключений.



from multiprocessing.pool import Pool
from typing import Iterable, Callable
from multiprocessing import TimeoutError


def main(func: Callable, iterable: Iterable, timeout: int) -> list:
    with Pool() as pool:
        results = [pool.apply_async(func, (obj,)) for obj in iterable]
        for idx, unk in enumerate(results):
            try:
                state = unk.get(timeout)
            except TimeoutError:
                state = 'TimeoutError'
            finally:
                results[idx] = state
        return results