# Как Вы уже знаете в модуле нет аналога класса threading.Timer. Но это не проблема, можно написать такой класс самостоятельно.

# Ваша задача - написать класс процесса с отложенным запуском - Timer. Класс (как и аналог модуля threading) должен иметь два публичных метода:
# - метод запуска;
# - метод отмены.
# Конструктор предполагается вызывать со следующим синтаксисом:

# pr_timer = Timer(interval, function, args, kwarg)
# При вызове метода запуска start() вызывается метод run(), который ожидает завершения интервала таймаута и после этого 
# вызывает function(*args, **kwargs). Метод cancel сбрасывает таймер.



from typing import Any, Callable, Sequence
from multiprocessing import Event, Process


class Timer(Process):
    def __init__(
        self,
        interval: int | float,
        function: Callable[[Any], Any],
        args: Sequence[Any] | None = None,
        kwargs: dict[Any, Any] | None = None,
    ) -> None:
        self.interval = interval
        self.function = function
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}
        self.finished = Event()
        super().__init__()

    def cancel(self):
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()