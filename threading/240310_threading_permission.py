# перепишите функцию permission так, чтобы целевую задачу выполнил успешно только второй по очередности поток, 
# вызвавший проверку условия, причем только со второго раза после истечения таймера. Только допишите необходимую 
# логику в функции и все, что она может еще использовать. Все что уже задано  - изменять нельзя. И сам класс и 
# создание и запуск нескольких потоков - все определено в тестирующей системе.

# Гарантируется, что будет создано и запущено два или более потоков в период до истечения таймаута ожидания условия.


import threading
from typing import Callable
from time import perf_counter
from itertools import count


class TestWorker(threading.Thread):
    def __init__(self, task: Callable, permission: Callable, condition: threading.Condition):
        super().__init__()
        self.permission = permission
        self.task = task
        self.condition = condition

    def make_work(self):  # основной метод выполняет задачу если получено условие
        with self.condition:
            start = perf_counter()
            tmp = self.condition.wait_for(predicate=self.permission, timeout=5)
            if tmp:
                self.task()  # выполняем задачу если разрешено
            else:
                # не выполняем задачу, просто логируем, что не дождались условия и выводим время
                print(f"escaping by timer with {threading.current_thread().name=}, {perf_counter() - start}")

    def run(self):
        self.make_work()


def task():
    print(f"working task with {threading.current_thread().name=}")


_count = count(1)
condition = threading.Condition()


def permission():
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"calling permission {n} with {thread_name}")
    return n > 2 and '2' in thread_name