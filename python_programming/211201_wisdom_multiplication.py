# Умножение по "схеме мудреца" с конкатенацией.
# Напишите функцию wisdom_multiplication(x, y, length_check = True), реализующую умножение по схеме мудреца с прошлого шага.

# Вычитаем из 100 первое и второе число.
#  -Складываем результаты шага 1.
#  -Вычитаем из 100 результат шага 2.
#  -Перемножаем результаты шага 1.
# Результат шага 3 даёт первые цифры результата, а результат шага 4 даёт последние 2 цифры результата. В зависимости от
# значения аргумента length_check функция проверяет или нет длину результата шага 4 и при необходимости дописывает 0 перед
# ним (если результат всего 1 цифра). Функция должна возвращать целое число.

# Sample Input 1:
# 96x97

# Sample Output 1:
# 9312

# Sample Input 2:
# 99x99
# length_check=True

# Sample Output 2:
# 9801

# Sample Input 3:
# 99x99
# length_check=False

# Sample Output 3:
# 981

# Sample Input 4:
# 10x10

# Sample Output 4:
# -808100

# Sample Input 5:
# 91x99

# Sample Output 5:
# 9009

def wisdom_multiplication(x, y, length_check=True):
    x1, y1 = 100-x, 100-y
    sub = 100 - (x1 + y1)
    prod = x1 * y1
    if length_check:
        if len(str(x * y)) <= len(''.join([str(sub), str(prod)])):
            return int(''.join([str(sub), str(prod)]))
        else:
            return int(''.join([str(sub), '0', str(prod)]))
    else:
        return int(''.join([str(sub), str(prod)]))