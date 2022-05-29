# Consider the following:
# A string, s, of length n where s = c0c1.....cn-1.
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s.
# Then, use each ti to create string ui such that:
# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
# In other words, if the character at some index j in ti occurs at a previous index<j in ti, then do not include the
# character in string ui.
# Given s and k, print n/k lines where each line i denotes string ui.

# Sample Input:
# AABCAAADA
# 3

# Sample Output:
# AB
# CA
# AD

def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub = s[i:i + k]
        unique_sub = ''
        for c in sub:
            unique_sub += c if not c in unique_sub else ''
        print(unique_sub)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)