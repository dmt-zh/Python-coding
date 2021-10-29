# На вход подаётся 1 строка, слова в которой разделены пробелами.
# Напечатайте через пробел число слов в строке и число слов "one" в строке.

# Sample Input 1:
# One string short and one long

# Sample Output 1:
# 6 1

# Sample Input 2:
# one cat and one dog are friends

# Sample Output 2:
# 7 2

(lambda x: print(len(x), x.count('one')))(input().split())