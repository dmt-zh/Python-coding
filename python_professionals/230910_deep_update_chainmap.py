# Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

# chainmap — объект типа ChainMap, элементами которого являются словари
# key — хешируемый объект
# value — произвольный объект

# Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. Если ключ key отсутствует в chainmap,
# функция должна добавить пару key: value в первый словарь.

# Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.
# Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.


from collections import ChainMap
from typing import Any, Dict, Iterable


def deep_update(chain_obj: Iterable[Dict], key: str, value: Any) -> None:
    if not key in chain_obj:
        chain_obj[key] = value
    [dict_.update({key: value}) for dict_ in chain_obj.maps if key in dict_]
    return
