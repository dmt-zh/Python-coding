# Given a list of rational numbers,find their product.

# Sample Input 0
# 3
# 1 2
# 3 4
# 10 6

# Sample Output 0
# 5 8

from fractions import Fraction
from functools import reduce
import math

def product(fracs):
    t = math.prod(fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)