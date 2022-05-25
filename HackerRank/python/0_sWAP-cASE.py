# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# - string s: the string to modify
# Returns string: the modified string

# Input Format
# A single line containing a string s.

# Sample Input 0
# HackerRank.com presents "Pythonist 2".

# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    swaped = ''
    for i in s:
        if i.islower():
            swaped += i.upper()
        else:
            swaped += i.lower()
    return swaped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)