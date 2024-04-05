# Напишите функцию и организуйте обработку не перехваченных исключений.

# Создание и запуск дополнительного потока для проверки обработки не перехваченных исключений будет выполнено тест. системой.

# Теперь функция обработки сложнее. Если тип исключения TypeError или ValueError - то необходимо просто выводить информацию об
# ошибке в консоль. Если исключение другого типа - то необходимо создать файл custom_errors.txt и уже туда записать информацию об ошибке.
# Информация об ошибке для двух источников вывода - одинакова!

# Информация об ошибке это строка, которая формируется по шаблону:
# <thread_name>, <type_error_name>, <msg>



import threading


def custom_hook(args):
    exc_type, exc_value, _, exc_thread = args
    log = f'{exc_thread.name}, {exc_type.__name__}, {exc_value}'
    if exc_type in (TypeError, ValueError):
        print(log)
        return
    with open('custom_errors.txt', 'a', encoding='utf8') as logger:
        logger.write(f'{log}\n')
        
threading.excepthook = custom_hook