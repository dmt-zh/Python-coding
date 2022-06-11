# You are given a set A and N number of other sets. These N number of sets have to perform some
# specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.

# Sample Input
#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66

# Sample Output
# 38

i = int(input().strip())
A = set(map(int, input().strip().split()))
n = int(input().strip())

for _ in range(n):
    command = input().strip().split()[0]
    new_set = set(map(int, input().strip().split()))
    if command.startswith('update'):
        A.update(new_set)
    elif command.startswith('inter'):
        A.intersection_update(new_set)
    elif command.startswith('diff'):
        A.difference_update(new_set)
    else:
        A.symmetric_difference_update(new_set)

print(sum(A))