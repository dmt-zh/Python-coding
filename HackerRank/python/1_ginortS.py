# You are given a string S.
# S contains alphanumeric characters only.

# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Sample Input
# Sorting1234

# Sample Output
# ginortS1324

s = input().strip()

lower = ''
upper = ''
digits = []


for i in s:
    if i.isalpha() and i.islower():
        lower += i
    elif i.isalpha() and i.isupper():
        upper += i
    else:
        digits.append(int(i))

sorted_lower = ''.join(sorted(lower))
sorted_upper = ''.join(sorted(upper))
sorted_digits = ''.join(map(str, sorted(sorted(digits), key=lambda x: x % 2, reverse=True)))

print(sorted_lower + sorted_upper + sorted_digits)