# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.

# Пример:
# s = "abababa"
# t = "aba"

# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

# Sample Input 1:
# abababa
# aba

# Sample Output 1:
# 3

str, sub = (input() for _ in range(2))
print(len([i for i in range(len(str)) if str.startswith(sub, i)]))