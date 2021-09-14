from collections import deque

# простой граф
graph = {
    'A': ['B', 'C', 'D'], 'B': ['F'], 'C': ['B', 'E'],
    'D': ['E'], 'E': ['L', 'K'], 'F': ['O', 'L'],
    'L': ['end'], 'K': ['L', 'P'], 'O': ['end'], 'P': ['end']
}

def find_end(char):                                 # функция поиска слова "end"
    if 'end' in char:
        return True
    return False

def search_way(start):
    search_queue = deque()                          # cоздание новой очереди
    search_queue += graph[start]                    # все соседи добавляются в очередь поиска
    searched = []                                   # массив для отслеживания уже проверенных точек
    while search_queue:                             # пока очередь не пуста ...
        point = search_queue.popleft()              # из очереди извлекается первая точка
        if not point in searched:                   # проверяем, содержит ли точка конец
            if find_end(point):
                return f'Found the "end"!'          # да, эта точка содержит "end"
            else:                                   # если нет...
                search_queue += graph[point]        # все соседи этой точки добавляются в очередь поиска
                searched.append(point)              # добавляем точку в массив уже проверенных


print(search_way('A'))