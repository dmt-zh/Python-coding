# Первое качество пула процессов - экономное и эффективное использование рабочих процессов мы реализовали. Теперь попробуем
# сделать следующих шаг - получить результат обработки задач. Как Вы помните по пулу потоков, было очень просто получить результаты 
# функций, которую выполняют несколько потоков, используя определенные методы. Напишем такой метод.

# Ваша задача написать класс SimplePool, который повторяет функционал предыдущего задания, но также позволяет возвращать результат работы задач.

# Класс должен иметь публичные атрибуты и методы:
# Уже известные по пред. заданию атрибут max_workers;
# Метод map(), который получает два аргумента: task, args и возвращает список результатов выполнения функции task для каждого набора аргументов.
# Список результатов должен формироваться в том же порядке, в каком расположены аргументы в коллекции args.
# Класс должен поддерживать следующий синтаксис конструктора и обращений к методу:

# s_pool = SimplePool(5) # указываем max_workers = 5
# s_pool = SimplePool(max_workers = 5) # указываем max_workers = 5
# s_pool = SimplePool() # max_workers = количеству ядер на испольняемой машине

# result = s_pool.map(task=my_function, args=(22.2, 0.1, 5, 6))
# Тестирующая система создаст несколько экземпляров класса SimplePool, проверит время выполнения и результат решения.



from typing import Any, Callable, Optional, Sequence
from os import cpu_count
from multiprocessing import Process, current_process, Manager
from math import ceil
from random import uniform
from time import sleep


class SimplePool:
    def __init__(
        self,
        max_workers: Optional[int] = None,
    ) -> None:
        self.max_workers = cpu_count() or 1 if max_workers is None else max_workers
        self._sinc_dict = Manager().dict()

    def _args_grouper(
        self,
        num_workers: int,
        args_to_group: Sequence[Any],
    ) -> Sequence[Sequence[Any]]:
        groups = []
        quotient, remainder = ceil(len(args_to_group) / num_workers), len(args_to_group) % num_workers
        pointer = 0
        for number in range(num_workers):
            group_window = quotient if number < remainder else quotient - 1
            groups.append(args_to_group[pointer:pointer + group_window])
            pointer += group_window
        return groups

    def _runner(
        self,
        task: Callable[[Any], Any],
        args: Sequence[Any],
    ) -> None:
        for arg in args:
            self._sinc_dict[arg] = task(arg)

    def map(
        self,
        task: Callable[[Any], Any],
        args: Sequence[Any],
    ) -> Sequence[tuple[int, Any]]:
        processes = []
        for task_args in self._args_grouper(self.max_workers, args):
            processes.append(Process(target=self._runner, args=(task, task_args,)))
            processes[-1].start()
        for process in processes:
            process.join()
        return (self._sinc_dict.get(arg) for arg in args)


def task(arg):
    sleep(uniform(0, 1))
    return current_process().ident, arg


if __name__ == "__main__":
    args = [3, 2, 1, 5, 6, 7, 4]
    my_pool = SimplePool(3)
    for _id, v in my_pool.map(task=task, args=args):
        print(f"ident={_id}, {v}")