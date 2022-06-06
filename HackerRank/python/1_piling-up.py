# There is a horizontal row of n cubes. The length of each cube is given.
# You need to create a new vertical pile of cubes. The new pile should follow these directions:
# if cubei is on top of cubej then sideLengthj >= sideLengthi.
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
# Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

# Sample Input
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]

# Sample Output
# Yes
# No

from collections import deque
stack = []

T = int(input().strip())
for _ in range(T):
    n = input()
    cubes = deque(map(int, input().strip().split()))
    ans = 'Yes'
    right = cubes.pop()
    left = cubes.popleft()
    stack.append(max(right, left))
    length = len(cubes)
    max_el = max(left, right)
    while length > 1:
        r = cubes.pop()
        l = cubes.popleft()
        max_el = max(l, r)
        length = len(cubes)
        if max_el > stack[-1]:
            ans = 'No'
            break
        else:
            stack.append(max_el)
            continue
    if length == 0 and max_el > stack[-1]:
        ans = 'No'
    if length > 0 and cubes[-1] > stack[-1]:
        ans = 'No'
    stack.clear()
    print(ans)