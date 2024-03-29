# В онлайн-школе BEEGEEK каждое лето проходят соревнования по шахматам, во время которых ведется статистика побед и
# поражений. Каждая партия описывается кортежем из двух элементов, где первый элемент — имя победившего ученика,
# второй элемент — имя проигравшего ученика.

# Реализуйте функцию wins(), которая принимает один аргумент:
# pairs — итерируемый объект, элементами которого являются кортежи, каждый из которых представляет собой пару имён
# победитель-проигравший
# Функция должна возвращать словарь, в котором ключом служит имя ученика, а значением — множество (тип set) имен учеников,
# которых он победил.



from typing import Dict, Sequence, Set, Tuple
from collections import defaultdict

def wins(pairs: Sequence[Tuple[str, str]]) -> Sequence[Dict[str, Set[str]]]:
    table = defaultdict(set)
    for pair in pairs:
        table[pair[0]].add(pair[-1])
    return table