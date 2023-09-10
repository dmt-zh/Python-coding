# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект

# Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
# Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.



from typing import Dict, Iterable

def get_all_values(chain_obj: Iterable[Dict], key: str) -> set:
    return set(filter(None, (obj.get(key, None) for obj in chain_obj.maps)))