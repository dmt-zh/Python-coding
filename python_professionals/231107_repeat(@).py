# Реализуйте декоратор repeat, который принимает один аргумент:

# times — натуральное число
# Декоратор должен вызывать декорируемую функцию times раз.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.



from functools import wraps

def repeat(times):
    def call_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return call_func