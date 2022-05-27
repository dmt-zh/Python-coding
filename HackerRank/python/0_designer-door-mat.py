# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:

# Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Sample Input
# 9 27

# Sample Output
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

n, m = map(int, input().split())
width = tuple(i for i in range(1, n, 2))

for i in range(n):
    middle = n // 2
    if i < middle:
        s = '.|.' * width[i]
        print(s.center(m, '-'))
    elif i == middle:
        print('WELCOME'.center(m, '-'))
    else:
        idx = (i - len(width)) * - 1
        s = '.|.' * width[idx]
        print(s.center(m, '-'))