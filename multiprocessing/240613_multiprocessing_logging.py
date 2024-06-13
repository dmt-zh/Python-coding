# Итак, перепишите предыдущее решение, добавив логирование ошибок для вызова каждой потенциально проблемной
# функции: get_image, image_processing, save_image. Позволим себе некоторое упрощение и предположим, что все возможные ошибки
# обязательно будут из группы Exception. И что для обработки ошибок достаточно применить стандартную конструкцию try except при
#  попытке вызова каждой из функций.

# В результате Вашей доработки в случае ошибок при вызове любой из трех перечисленных функций должен быть сформирован файл
# ошибок log_errors.txt, с сообщениями вида:
# <имя процесса>, <метка времени>, <имя функции>, <ошибка> где <имя процесса> - очевидно имя процесса, который вызвал функцию;
# <метка времени> - метка времени вызова (используйте или стандартный asctime или datetime.now());
# <имя функции> - имя функции (можно получить через дандер метод .__name__);
# <ошибка> - сообщение об ошибке.



import concurrent.futures
import logging
from functools import wraps
from datetime import datetime
from multiprocessing import get_logger as mp_get_logger
from pathlib import Path


logger = mp_get_logger()
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler('log_errors.txt')
file_handler.setFormatter(logging.Formatter(fmt='{processName}, {asctime}, {message}', style='{'))
logger.addHandler(file_handler)

def log_wrapper(func: callable):
    wraps(func)
    def wrapper(*args, **kwds):
        try:
            return func(*args, **kwds)
        except Exception as err:
            logger.error(f'{datetime.now()}, {func.__name__}, {err}')
    return wrapper

get_image = log_wrapper(get_image)
image_processing = log_wrapper(image_processing)
save_image = log_wrapper(save_image)

def _processor(url: str) -> str:
    file_to_process = get_image(url)
    return image_processing(file_to_process)

def _image_uploader(future: concurrent.futures.Future) -> None:
    _file = future.result()
    save_image(_file)

def group_image_processing(config) -> None:
    with open(config, encoding='utf8') as fin:
        urls_to_handle = (url.rstrip() for url in fin.readlines())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for url in urls_to_handle:
            executor.submit(_processor, url).add_done_callback(_image_uploader)