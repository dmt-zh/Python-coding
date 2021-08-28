# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
# частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
# лексикографически первое (можно использовать оператор < для строк).
# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC

# Sample Output:
# abc 3

file_path = 'dataset_3363_3.txt'
fin = open(file_path)
raw_text = fin.read()

import re
text = re.split('[^a-zA-Z]', raw_text)
lst = [i.lower() for i in (filter(None, text))]

from collections import Counter
word = Counter(lst).most_common()[:-2:1][0]
print(word[0], word[1])
