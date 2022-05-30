# In this challenge, you will be given 2 integers, n and m. There are n words,
# which might repeat, in word group A. There are m words belonging to word group B.
# For each m words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of m in group A. If it does not appear, print -1.

# Example
# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
# For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
# The second word, 'c', does not appear in group A, so print -1.

# Expected output:
# 1 3
# -1

from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for idx in range(1, n + 1):
    char = input().strip()
    if not char in d:
        d[char] = [idx]
    else:
        d[char].append(idx)

for _ in range(m):
    word = input().strip()
    if isinstance(d[word], list):
        print(*d[word], sep=' ')
    else:
        print(d[word])