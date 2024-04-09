# Напишите функцию отложенного запуска delayed_launch(initializer: Callable, task: Callable, permission: Callable),
# которая позволяет запускать задачу инициализатора initializer в отдельном потоке, периодически проверяет разрешение
# permission и, когда разрешение получено, запускает основную задачу task. Функции initializer, task, permission не принимают аргументов!

# Функция должна:
#     Создавать и использовать примитив синхронизации Event.
#     Запускать рабочий поток, который выполняет (вызывает) функцию инициализатора initializer, а затем ждет разрешения (события Event),
#     чтобы вызвать основную функцию task.
#     Запускать еще один контрольный поток, который в цикле вызывает функцию permission до тех пор, пока она не вернет True. 
#     Функция permission возвращает True, если разрешение получено, или False - если еще нет. Если разрешение получено, контрольный
#     поток должен разрешить выполнить основную задачу рабочему потоку.

# Напишите функцию согласно условию задания. Ваше решение, при необходимости, может включать в себя другие вспомогательные функции.
# Тестирующая система вызовет Вашу функцию с различными аргументами initializer, task, permission и проверит ее работу.
# Передаваемые в аргументы функции initializer, task, permission определены в тестирующей системе.


import threading
from typing import Callable


def runner(initializer: Callable, task: Callable, event: threading.Event):
    initializer()
    event.wait()
    task()

def get_permission(permission: Callable, event: threading.Event):
    has_permission = False
    while not has_permission:
        has_permission = permission()
    event.set()

def delayed_launch(initializer: Callable, task: Callable, permission: Callable) -> None:
    event = threading.Event()
    main_thread = threading.Thread(target=runner, args=(initializer, task, event))
    main_thread.start()

    dummy_thread = threading.Thread(target=get_permission, args=(permission, event), daemon=True)
    dummy_thread.start()