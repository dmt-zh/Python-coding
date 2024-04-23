# Напишите класс для параллельной обработки задач ParallelExecuter, который меет атрибуты:
# log - список со статусом исполнения каждой задачи. Длина списка равна количеству объектов - задач;
# timeout - значение таймаута (int, float, значение по умолчанию - None).

# При необходимости можно создавать дополнительные атрибуты.
# Конструктор класса должен принимать:
# - ​​​​​​список или кортеж вызываемых объектов - задач,
# - список или кортеж из аргументов для каждой задачи (каждая задача может иметь несколько аргументов!). Для решения достаточно предусмотреть
#   только передачу позиционных аргументов;
# - не обязательный аргумент - timeout, уставка максимального времени ожидания завершения всех задач. 
#   Если аргумент не задан - время ожидания не ограничено. Если аргумент задан (int, количество секунд), то выполняется контроль длительности
#   выполнения задач. Если за отведенное время задачи не успевают завершиться, процесс, который выполняет такую длительную задачу, должен быть
#   завершен принудительно.
# Во время запуска методом execute() создает отдельный процесс для выполнения каждой из задач.
# После создания и запуска всех дочерних процессов обработки ожидает необходимый таймаут и проверяет статус каждого процесса выполнения задачи. 
# Если процесс все еще выполняется, считаем, что он "завис", его нужно принудительно завершить и очистить его ресурсы, в лог для такой задачи в
# качестве значения устанавливается текст: <task> processing timeout exceeded где <task> - имя задачи (task.name), на котором "завис" процесс.
# Если задача завершилась вовремя, в список лога добавляется: <task> completed successfully
# Порядок значений в логе должен соответствовать порядку переданных в конструктор задач на исполнение.
# Не используйте функцию sleep.


import multiprocessing
from typing import Any, Callable, Sequence, TypeAlias, Union
from threading import Thread
from threading import Timer

TaskArgs: TypeAlias = Sequence[Any]
ExecutedTask: TypeAlias = Callable[[TaskArgs], Any]
TaskTimeout: TypeAlias = Union[int, float, None]

class ParallelExecuter:
    def __init__(
        self, 
        tasks: Sequence[ExecutedTask],
        tasks_args: Sequence[TaskArgs],
        timeout: TaskTimeout = None,
    ) -> None:
        self.tasks = tasks
        self.tasks_args = tasks_args
        self.timeout = timeout
        self.log = []

    def _break_processing(self, processes: Sequence[multiprocessing.Process]) -> None:
        for process in processes:
            if process.is_alive():
                process.terminate()
                process.join()
                process.close()
                self.log.append(f'{process.name} processing timeout exceeded')
            else:
                self.log.append(f'{process.name} completed successfully')

    def execute(self):
        handlers = []
        for task, task_args in zip(self.tasks, self.tasks_args):
            handlers.append(multiprocessing.Process(target=task, args=task_args, name=task.__name__))
            handlers[-1].start()

        if self.timeout:
            thread_timer = Timer(self.timeout, function=self._break_processing, args=(handlers,))
            thread_timer.start()
            thread_timer.join()
            return

        for handler in handlers:
            self.log.append(f'{handler.name} completed successfully')
            handler.join()
            handler.close()