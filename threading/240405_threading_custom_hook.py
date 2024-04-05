# Напишите функцию обработки не перехваченных исключений и переопределите threading.excepthook на нее.
# Кастомная функция обработки очень простая. Все что она делает - это печать в консоль сообщение исключения (exc_value).
# Создание и запуск дополнительного потока для проверки обработки не перехваченных исключений будет выполнено тест. системой.


import threading


def custom_hook(args):
    _, exc_value, _, _ = args
    print(exc_value)

threading.excepthook = custom_hook