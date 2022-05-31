# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

n = int(input().strip())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(*sorted([*(a - b), *(b - a)]), sep='\n')