# Реализуйте функцию caesar(text, key), возвращающую зашифрованный текст, работающую только с латинским алфавитом.
# text - исходных текст, который надо зашифровать (или расшифровать)
# key - ключ (сдвиг)
# Ключ может быть отрицательным или больше 26. Из преобразуемого текста удаляются все пробелы и знаки препинания.
# Зашифрованный текст пишется в верхнем регистре 1 строкой. Необходимо только реализовать функцию.

# Sample Input 1:
# 3
# Ave, Caesar

# Sample Output 1:
# Encrypted: DYHFDHVDU
# Decrypted back: AVECAESAR

# Sample Input 2:
# -3
# dyhfdhvdu

# Sample Output 2:
# Encrypted: AVECAESAR
# Decrypted back: DYHFDHVDU

# Sample Input 3:
# 13
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

# Sample Output 3:
# Encrypted: GURDHVPXOEBJASBKWHZCFBIREGURYNMLQBT
# Decrypted back: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG

import string
import re

def caesar(text, key):
    letters = string.ascii_uppercase
    upper = re.sub(r'\W+', '', text).upper()
    return ''.join([letters[(letters.index(i) + key) % len(letters)] for i in upper])