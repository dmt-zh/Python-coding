# На вход подаётся 1 строка, слова в которой разделены пробелами.
# Напечатайте слова из этой строки в обратном порядке, используя в качестве разделителя "-$-"

# Sample Input:
# one two three four five six

# Sample Output:
# six-$-five-$-four-$-three-$-two-$-one


print('-$-'.join(input().split()[::-1]))