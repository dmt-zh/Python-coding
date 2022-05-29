# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Sample Input
# HACK 2

# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

from itertools import combinations
s, n = input().strip().split()

for i in range(1, int(n) + 1):
    print(*[''.join(elem) for elem in list(combinations(sorted([i for i in s]), i))], sep='\n')