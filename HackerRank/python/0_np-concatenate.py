# You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column).
# Your task is to concatenate the arrays along axis 0.

# Input Format
# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.

# Output Format
# Print the concatenated array of size X.

# Sample Input
# 4 3 2
# 1 2
# 1 2
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4

# Sample Output
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]

import numpy as np

n, m, p = list(map(int, input().strip().split(' ')))
A = np.array([list(map(int, input().strip().split(' '))) for _ in range(n)])
B = np.array([list(map(int, input().strip().split(' '))) for _ in range(m)])

print(np.concatenate((A, B), axis=0))