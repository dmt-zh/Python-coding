# Реализуйте функцию jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False), возвращающую
# зашифрованный текст, по алгоритму описанному на предыдущем шаге:
# text - исходный текст
# key - ключ шифрования (число)
# alphabet - алфавит (по умолчанию английский)
# reverse - признак расшифровки, если находится в значении True, это значит, что функцию надо использовать для расшифровки
# текста, т.к. каждый сдвиг должен быть отрицательным. (по умолчанию False). Из преобразуемого текста удаляются все пробелы
# и знаки препинания. Зашифрованный текст пишется в верхнем регистре 1 строкой.

# Sample Input 1:
# У СУДЬИ ЖАРРИКЕСА ПРОНИЦАТЕЛЬНЫЙ УМ
# 423
# АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
# reverse=False

# Sample Output 1:
# ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР

# Sample Input 2:
# ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР
# 423
# АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
# reverse=True

# Sample Output 2:
# УСУДЬИЖАРРИКЕСАПРОНИЦАТЕЛЬНЫЙУМ

# Sample Input 3:
# Some encripted text for this assignment
# 26101986

# Sample Output 3:
# UUNEFWKXKVUEECMDVLPRUQQYCYTIHWUKPZ

def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    upper = ''.join([i for i in text.upper() if i.isalnum()])
    n = len(upper) // len(str(key)) + 1
    code = (n * str(key))[:len(upper)]
    flag = -1 if reverse else 1
    return ''.join([alphabet[(alphabet.find(i) + flag * int(j)) % len(alphabet)] for i, j in zip(upper, code)])