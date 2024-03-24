# В тестирующей системе задан список ресурсов sources. Определена функция get_request_header, принимающая
# в качестве аргумента элемент из списка ресурсов.

# С помощью пула потоков создайте необходимое количество рабочих потоков, запустите задачи с использованием
# метода submit(). Также реализуйте условие: если ответ от ресурса превышает 1,5 секунды, не дожидаться ответа
# от ресурса. Вместо заголовков для ресурсов, ответ от которых превышает этот лимит, следует заполнять строковым
# значением "no_response".

# Ханилище заголовков headers_stor должен быть сформирован за время не превышающее ~1.5 секунды.



import concurrent.futures


headers_stor = {url: 'no_response' for url in sources}

executor = concurrent.futures.ThreadPoolExecutor()
try:
    future_works = {executor.submit(get_request_header, url): url for url in sources}
    done, not_done = concurrent.futures.wait(future_works.keys(), timeout=1.5)
    for future in done:
        value = future_works.get(future)
        headers_stor[value] = future.result()
finally:
    executor.shutdown(wait=False, cancel_futures=True)