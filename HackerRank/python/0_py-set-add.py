# Rupal has a huge collection of country stamps. She decided to count the total number
# of distinct country stamps in her collection. She asked for your help. You pick the
# stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France

# Sample Output
# 5

n = int(input().strip())
print(len(set(input().strip() for i in range(n))))