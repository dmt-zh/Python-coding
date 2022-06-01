# Task
# You have a non-empty set S, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
# Print the sum of the elements of set S on a single line.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

# Sample Output
# 4

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input().strip())):
    command = input().split()
    if command[0].startswith('rem'):
        s.remove(int(command[1]))
    elif command[0].startswith('pop'):
        s.pop()
    else:
        s.discard(int(command[1]))

print(sum(s))