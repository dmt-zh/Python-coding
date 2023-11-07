# Реализуйте декоратор returns, который принимает один аргумент:

# datatype — тип данных
# Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. 
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.



from functools import wraps

def returns(datatype):
    def call_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if not isinstance(func_result, datatype):
                raise TypeError
            return func_result
        return wrapper
    return call_func