# You are given a list of N lowercase English letters. For a given integer K,
# you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
# Find the probability that at least one of the K indices selected will contain the letter: 'a'.

from itertools import combinations

n = input()
arr = input().strip().split()
k = int(input())

a = 0
cnt = 0
for i in combinations(arr, k):
    if 'a' in i:
        a += 1
    cnt += 1

print(f'{a/cnt:.3f}')