# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.

# Example
# Set ([1, 3, 4]) is a strict superset of set ([1, 3]).
# Set ([1, 3, 4]) is not a strict superset of set ([1, 3, 4]).
# Set ([1, 3, 4]) is not a strict superset of set ([1, 3, 5]).

A = set(map(int, input().strip().split()))
res = False
for s in range(int(input())):
    s = set(map(int, input().strip().split()))
    if A.issuperset(s):
        res = True
    else:
        res = False
        break

print(res)