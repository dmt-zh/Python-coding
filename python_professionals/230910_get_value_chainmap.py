# Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# from_left — булево значение, по умолчанию равное True

# Функция должна возвращать значение по ключу key из chainmap, причем:
# если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
# если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
# Если ключ key отсутствует в chainmap, функция должна вернуть значение None.


from collections import ChainMap
from typing import Any, Dict, Iterable


def get_value(chain_obj: Iterable[Dict], key: Any, from_left: bool = True) -> None | Any:
    return chain_obj.get(key) if from_left else ChainMap(*chain_obj.maps[::-1]).get(key)