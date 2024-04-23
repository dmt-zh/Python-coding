# Напишите класс специализированного процесса - обработчика CSV файлов CSVHandler, который:

# * Наследуется от Process.
# * Имеет дополнительные атрибуты:
#     -> files - коллекция (list, tuple) с именами файлов для обработки;
#     -> worker - функция обработки (вызываемый объект). Единственный аргумент функции принимает название файла;
#     -> timeout - значение таймаута (int, float, значение по умолчанию 1 секунда,).
#   При необходимости можно создавать дополнительные атрибуты.
# * Во время запуска создает отдельный дочерний процесс обработки для каждого файла.
# * После создания и запуска всех дочерних процессов обработки ожидает необходимый таймаут и проверяет статус каждого процесса обработки.
#   Если процесс все еще занимается обработкой, считаем, что он "завис", его нужно принудительно завершить и очистить его ресурсы, также
#   выполняется вывод в консоль: <file> processing timeout exceeded
#   где <file> - имя файла обработки, на котором "завис" процесс.


import multiprocessing
from typing import Any, Callable, Sequence, TypeAlias
from time import sleep

AppliedWorker: TypeAlias = Callable[[str], Any]

class CSVHandler(multiprocessing.Process):
    def __init__(
        self,
        files: Sequence[str] | None = None,
        worker: AppliedWorker | None = None,
        timeout: int | float = 1,
    ) -> None:
        self.files = files
        self.worker = worker
        self.timeout = timeout
        super().__init__()

    def run(self) -> None:
        if not self.files or not self.worker:
            print(f'No files or worker to start the process.')
            return

        handlers = []
        for file in self.files:
            handlers.append(multiprocessing.Process(target=self.worker, args=(file,)))
            handlers[-1].start()

        sleep(self.timeout)

        for handler in handlers:
            if handler.is_alive():
                handler.terminate()
                handler.join()
                handler.close()
                print(f'{handler.name} processing timeout exceeded')