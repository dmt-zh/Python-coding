# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

from collections import deque

d = deque()
N = int(input().strip())
for _ in range(N):
    ins = input().strip()
    if ins.startswith('appendleft'):
        command, digit = ins.split()
        d.appendleft(int(digit))
    elif ins.startswith('append'):
        command, digit = ins.split()
        d.append(int(digit))
    elif ins.startswith('popleft'):
        d.popleft()
    else:
        d.pop()

print(*d)