# С помощью пула потоков создайте необходимое количество рабочих потоков, запустите задачи, после получения 
# результатов запустите пост обработчик. Если во время выполнения задачи возникают ошибки, выведите в консоль сообщение исключения.

# Напишите решение с использованием методов submit, exception, add_done_callback.

# В тестирующей системе задан список ресурсов sources, длина списка 5. Определена задача - функция worker, принимающая в качестве
#  аргумента элемент из списка ресурсов.

# В качестве задачи пост обработки напишите функцию post_worker. Все что она делает - печатает в консоль строку:
# <result> saved, если при получении результата не было ошибки.
# где <result> - результат, возвращаемый целевой функцией worker.



import concurrent.futures


def post_worker(future):
    broken_pipe = future.exception()
    if broken_pipe:
        print(broken_pipe)
        return
    print(f'{future.result()} saved')

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_works = [executor.submit(worker, src) for src in sources]
    for fw in future_works:
        fw.add_done_callback(post_worker)