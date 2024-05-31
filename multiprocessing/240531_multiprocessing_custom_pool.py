# Напишите простую реализацию пула процессов в виде функции pool(max_workers, task, args). Функция получает вызываемый объект задачи
# task (а по сути объект функции), которую необходимо многократно выполнить с использованием многопроцессорности. 
# Третий аргумент args - кортеж аргументов для этой функции. Например, если функция pool вызывается так:
# pool(task=my_function, args=(1, 4, 44.9)
     
# это значит, что my_function должна быть запущена с каждым набором аргументов из коллекции args:
# my_function(1), my_function(4), т.д.

# max_workers - указывает максимальное количество рабочих процессов в пуле. Это то количество рабочих процессов, которые будут выполнять задачи.
# Если число не указано, то оно должно быть равно количеству ядер на исполняемой машине.

# Если количество задач больше чем рабочих процессов в пуле, для каждого рабочего процесса должна быть сформирована группа задач на исполнение, свой блок задач.
# Блоки задач по количеству задач должны быть равны между рабочими процессами. Если разделение задач на блоки невозможно нацело, последнему 
# процессу достается меньшее количество задач в его блоке. Например, если количество аргументов равно 7 (нужно выполнить 7 задач-функций), а max_workers=3,
# то в очереди для первого рабочего потока будет 3 набора аргументов (для выполнения 3 задач), для 2 и 3 - по два набора.

# Гарантируется, что выполнение функций не будет завершаться ошибкой. Напишите функцию. Тестирующая система вызовет ее с различным набором аргументов,
# с различным количеством рабочих потоков. Проверяется время выполнения задач, время работы функции.



from typing import Any, Callable, Optional, Sequence
from os import cpu_count
from itertools import islice, repeat
from multiprocessing import Process, current_process
from math import ceil


def worker(
    func: Callable[[Any], Any],
    task_args: Sequence[Any],
) -> None:
    for tsk_arg in task_args:
        func(tsk_arg)

def pool(
    max_workers: Optional[int] = None,
    task: Optional[Callable[[Any], Any]] = None,
    args: Optional[Sequence[Any]] = None,
) -> None:
    if max_workers is None:
        max_workers = cpu_count() or 1

    def _args_grouper(num_workers: int, args_to_group: Sequence[Any]) -> Sequence[Sequence[Any]]:
        groups = []
        quotient, remainder = ceil(len(args_to_group) / num_workers), len(args_to_group) % num_workers
        pointer = 0
        for number in range(num_workers):
            group_window = quotient if number < remainder else quotient - 1
            groups.append(args_to_group[pointer:pointer + group_window])
            pointer += group_window
        return groups
    
    processes = []
    for task_args in _args_grouper(max_workers, args):
        processes.append(Process(target=worker, args=(task, task_args)))
        processes[-1].start()

    for process in processes:
        process.join()

def task(arg):
    print(f"ident={current_process().ident}, {arg}")


if __name__ == "__main__":
    args = [1, 2, 3, 4, 5, 6, 7]
    pool(max_workers=3, task=task, args=args)