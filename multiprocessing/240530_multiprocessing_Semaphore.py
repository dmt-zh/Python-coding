# Один из микросервисов, к которому обращается функция handler(elem) не может обработать более чем n=3 обращений одновременно.
# Нам снова нужна функция - обертка.

# Ваша задача написать функцию - обертку worker, которая:
# 1. Получает элемент из очереди elem_queue.
# 2. Передает элемент в функцию обработки handler.
# 3. После получения результата, добавляет его в очередь result_queue.
# 4. Гарантирует, что количество вызовов функции обработки handler для одновременного выполнения не будет превышать установленный порог.
# Допишите код согласно аннотации функции и шаблону задания. Не меняйте названия переменных, включая obj_lock.



import multiprocessing


def worker(
    elem_queue: multiprocessing.Queue,
    result_queue: multiprocessing.Queue,
    obj_lock: multiprocessing.Semaphore,
) -> None:
    with obj_lock:
        processed = handler(elem_queue.get())
        result_queue.put(processed)

if __name__ == "__main__":
    elem_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    obj_lock = multiprocessing.Semaphore(3)