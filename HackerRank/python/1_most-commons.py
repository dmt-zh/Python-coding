# A newly opened multinational brand has decided to base their company logo on the three most common
# characters in the company name. They are now trying out various combinations of company names and logos
# based on this condition. Given a string S, which is the company name in lowercase letters, your task is
# to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0
# aabbbccde

# Sample Output 0
# b 3
# a 2
# c 2

from collections import Counter
if __name__ == '__main__':
    s = Counter(input().strip())
    res = sorted(s.most_common(), key=lambda x: (-x[1], x[0]))[:3]
    for char in res:
        print(*char, sep=' ')