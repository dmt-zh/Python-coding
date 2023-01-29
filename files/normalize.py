# В файле in.txt записан текст. Проведите его нормализацию при помощи алгоритма NFKD.
# Результат запишите в переменную ans.


from unicodedata import normalize

with open('in.txt') as fin:
    ans = normalize("NFKD", fin.read())