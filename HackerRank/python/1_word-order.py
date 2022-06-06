# You are given N words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# Note: Each input line ends with a "\n" character.

# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1

from collections import OrderedDict

all_words = OrderedDict()
n = int(input().strip())
for _ in range(n):
    word = input().strip()
    if word in all_words:
        all_words[word] += 1
    else:
        all_words[word] = 1

print(len(all_words))
print(*all_words.values())