# Напишите кастомный класс WaitPool, с реализацией похожего метода wait. Кроме метода wait в классе должен быть реализован метод start,
# который создает и запускает пул процессов. Конструктор класса получает вызываемый объект - задачу и список или кортеж аргументов для задач.

# Подразумевается, что сначала будет вызван метод start, а только затем метод wait. Метод wait возвращает два списка с объектами AsyncResult. 
# В первом списке должны быть объекты с завершенными и успешно выполненными вызовами задачи task, во-втором, соответственно - не завершенные
# или завершенные с ошибкой. Класс WaitPool должен поддерживать контекстный менеджер.



from typing import Any, Callable, Final, NoReturn, Sequence
from multiprocessing.pool import Pool


class WaitPool(Pool):
    def __init__(
        self,
        task: Callable[[Any], Any],
        data: Sequence[Any],
        **kwargs: dict[str, Any],
    ) -> NoReturn:
        self._target: Final = task
        self._args: Final = data
        self._maped_async = None
        super().__init__(**kwargs)

    def start(self):
        self._maped_async = tuple(self.apply_async(self._target, (arg,)) for arg in self._args)

    def wait(self):
        done_tasks = tuple(_task for _task in self._maped_async if _task.ready() and _task.successful())
        not_done_tasks = tuple(filter(lambda _task: _task not in done_tasks, self._maped_async))
        return done_tasks, not_done_tasks
