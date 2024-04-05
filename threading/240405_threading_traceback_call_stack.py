# Напишите функцию и организуйте обработку не перехваченных исключений.

# Создание и запуск дополнительного потока для проверки обработки не перехваченных исключений будет выполнено тест. системой.

# Функция обработки не перехваченных исключений должна создавать файл <thread_name>.txt и уже туда записать весь 
# трейсбэк вызовов соответствующего потока, начиная от вызова целевой функции, и информацию об ошибке.

# Формат содержания файла лучше показать на примере.
# Если целевая функция потока имеет следующую вложенность вызовов:

# import threading

# # создайте функцию перехватчика исключений
# # переопределите функцию threading.excepthook

# def inner():
#     raise TypeError("message_error")

# def test_inner():
#     inner()

# def my_test():
#     test_inner()

# my_thread = threading.Thread(target=my_test, name="my_thread")
# my_thread.start()
# то в результате Вашей обработки не перехваченных исключений должен быть создан файл my_thread.txt, который содержит следующую информацию:

# Traceback:
# my_test -> test_inner -> inner
# Exception:
# TypeError: message_error



import threading
import traceback


def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    call_stack = ' -> '.join(frame[0].f_code.co_name for frame in [*traceback.walk_tb(exc_traceback)][2:])
    log = f'Traceback:\n{call_stack}\nException:\n{exc_type.__name__}: {exc_value}'
    with open(f'{exc_thread.name}.txt', 'w', encoding='utf8') as logger:
        logger.write(f'{log}')

threading.excepthook = custom_hook