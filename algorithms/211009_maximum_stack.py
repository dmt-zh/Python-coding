# Реализовать стек с поддержкой операций push, pop и max.
# Формат входа. Первая строка содержит число запросов q. Каждая из последующих q строк задаёт запрос в одном из
# следующих форматов: push v, pop, or max.
# Формат выхода. Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.
#
# Sample Input 1:
# 5
# push 2
# push 1
# max
# pop
# max

# Sample Output 1:
# 2
# 2

# Sample Input 2:
# 5
# push 1
# push 2
# max
# pop
# max

# Sample Output 2:
# 2
# 1

# Sample Input 3:
# 10
# push 2
# push 3
# push 9
# push 7
# push 2
# max
# max
# max
# pop
# max

# Sample Output 3:
# 9
# 9
# 9
# 9


import sys

stack = []
max_stack = []
curr_max = 0


for line in sys.stdin.readlines()[1:]:
    line = line.strip().split()
    if line[0] == 'push':
        curr_max = max(curr_max, int(line[1]))
        max_stack.append(curr_max)
        stack.append(int(line[1]))
    elif line[0].startswith('pop'):
        stack.pop()
        max_stack.pop()
        curr_max = max_stack[-1] if max_stack else 0
    elif line[0].startswith('max'):
        print(max_stack[-1] if max_stack else 0)
        