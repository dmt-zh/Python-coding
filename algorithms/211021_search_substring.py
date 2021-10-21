# Реализуйте алгоритм Карпа–Рабина.
# Формат входа. Образец Pattern и текст Text.
# Формат выхода. Индексы вхождений строки Pattern в строку Textв возрастающем порядке, используя индексацию с нуля.
# Ограничения. 1 ≤ |Pattern| ≤ |Text| ≤ 5 * 10^5.
# Суммарная длина всех вхождений образца в текста не превосходит 108. Обе строки содержат буквы латинского алфавита.

# Sample Input 1:
# aba
# abacaba

# Sample Output 1:
# 0 4

# Sample Input 2:
# Test
# testTesttesT

# Sample Output 2:
# 4

# Sample Input 3:
# aaaaa
# baaaaaaa

# Sample Output 3:
# 1 2 3


patt = input()
strng = input()

res = []
size = len(patt)

def make_hash(s):
    return sum(ord(char) for char in s)


def search_substring(s, sub):
    h_sub = make_hash(sub)
    h_s = make_hash(s[:size])
    if h_sub == h_s and patt == s[:size]:
        res.append(0)
    for pos in range(1, len(s)-size+1):
        h_s = h_s - ord(s[pos-1]) + ord(s[pos+size-1])
        if h_s == h_sub and patt == s[pos:pos+size]:
            res.append(pos)

search_substring(strng, patt)
print(*res)



# Тесты на time limit проходит и такая реализация:
ans = [i for i in range(len(strng)) if strng.startswith(patt, i)]
print(*ans)
