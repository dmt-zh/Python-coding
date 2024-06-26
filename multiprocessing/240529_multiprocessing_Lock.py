# В тестирующей системе заданы: функция handler(elem) - расчетная функция выполняемая процессами. 
# Преобразует элемент elem переданный ей из очереди и возвращает модифицированный элемент в качестве результата. 
# Также задана и наполнена элементами очередь, создан объект блокировки.

# from multiprocessing import Process, Lock, SimpleQueue

# lock = Lock()
# data = SimpleQueue()

# Ваша задача написать функцию - обертку worker, которая:
# 1. Получает элемент из очереди.
# 2. Передает элемент в функцию обработки handler.
# 3. После получения результата возвращает его обратно в очередь.
# 4. Гарантирует, что обработка одного элемента, включая получение из очереди элемента и отправка результата в очередь будет
# выполнена от начала и до конца одним потоком одного процесса в один момент времени.

# Так как очередь используется и для заданий и для результата, в конец очереди были добавлены элементы None. Если очередь возвращает элемент None,
# значит работу расчетных процессов нужно немедленно прекратить, все элементы обработаны.


from multiprocessing import Lock, SimpleQueue


def worker(lock: Lock, stor: SimpleQueue) -> None:
    while True:
        with lock:
            next_elem = stor.get()
            if next_elem is None:
                stor.close()
                break
            stor.put(handler(next_elem))