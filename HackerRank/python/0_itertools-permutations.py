# Task
# You are given a string S. Your task is to print all possible permutations of size k
# of the string in lexicographic sorted order.

# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

from itertools import permutations
s, n = input().strip().split()

lst = [''.join(i) for i in sorted(list(permutations(s, int(n))))]
print(*lst, sep='\n')