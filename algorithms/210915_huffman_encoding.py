# Задача на программирование: кодирование Хаффмана. По данной непустой строке s длины не более 10^4,
# состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код. В первой
# строке выведите количество различных букв kk, встречающихся в строке, и размер получившейся
# закодированной строки. В следующих k строках запишите коды букв в формате "letter: code". В последней
# строке выведите закодированную строку.


import heapq
from collections import Counter

def huffman_encoding(data):
    codes = dict.fromkeys(set(data), '') if len(set(data)) > 1 else {data[0]: '0'}
    heap = [(count, char) for char, count in Counter(data).items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node_one = heapq.heappop(heap)
        node_two = heapq.heappop(heap)
        new_node = (node_one[0] + node_two[0], node_one[1] + node_two[1])
        for letter in node_one[1]:
            codes[letter] = '0' + codes[letter]
        for letter in node_two[1]:
            codes[letter] = '1' + codes[letter]
        heapq.heappush(heap, new_node)
    return codes


s = input().strip()

out = huffman_encoding(s)
encoded = ''.join([out[i] for i in s])
print(len(out.keys()), len(encoded))
print(*[f'{k}: {v}' for k, v in out.items()], sep='\n')
print(encoded)
