# Ваша задача - написать функцию параллельной потоковой обработки файлов фотографий group_image_processing.
# Сырые файлы фотографий в формате raw хранятся на внешнем ресурсе и после обработки новые файлы нужно загрузить на внешнее хранилище.
# Ссылки на сырые файлы хранятся в локальном конфигурационном файле.

# При этом уже написаны и готовые следующие функции:
# функция получения фотографии по ссылке get_image(url: str) -> str. По указанной ссылке url скачивает файл и возвращает файл сырой
# фотографии (имя файла фотографии).
# функция обработки сырой фотографии image_processing(file: str) - > str. Обрабатывает указанный файл сырой фотографии, создает новый
# файл фотографии и возвращает имя нового файла.
# функция сохранения фотографии на внешнее хранилище save_image(file: str) - > None. Загружает на внешний ресурс указанный файл фотографии.
# С такими условиями эта задача прекрасно укладывается в концепцию применения пула процессов. Ведь в функции group_image_processing всего-лишь нужно:
# получить список ссылок из файла конфигурации (обычный текстовый файл) переданный в единственный аргумент функции, где каждая строка файла конфигурации - это отдельная ссылка

# написать целевую функцию, которую будту выполнять рабочие процессы пула.
# написать функцию коллбэка загрузки полученного в результате обработки файла фотографии.
# используя пул процессов запустить задачи, чтобы они выполнялись по готовности: что загрузил - то обработал, что обработал - то отправил на сохранение на внешний ресурс.



import concurrent.futures
from pathlib import Path
from typing import NoReturn


def _processor(url: str) -> str:
    file_to_process = get_image(url)
    return image_processing(file_to_process)

def _image_uploader(future: concurrent.futures.Future) -> NoReturn:
    _file = future.result()
    save_image(_file)

def group_image_processing(config: str) -> NoReturn:
    with open(config, encoding='utf8') as fin:
        urls_to_handle = (url.rstrip() for url in fin.readlines())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for url in urls_to_handle:
            executor.submit(_processor, url).add_done_callback(_image_uploader)