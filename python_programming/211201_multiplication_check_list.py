# Пакетная проверка "схемы мудреца" с конкатенацией.
# Пришло время модифицировать функции из задач на проверку схемы с учётом конкатенации.
# Напишите 2 функцию multiplication_check_list(start=10, stop=99, length_check = True)
# Для проверки всех пар в интервале.
# В зависимости от значения аргумента length_check добавляйте при необходимости 0 при конкатенации.

# multiplication_check_list должна уметь печатать:
#  -Правильных результатов: n
#  -Неправильных результатов: m

# Примечание. Пары, где числа поменялись местами считаются РАЗНЫМИ.
# Например, в интервале от 11 до 13 есть 9 пар:
# 11х11, 11х12, 11х13, 12х11, 12х12, 12х13, 13х11, 13х12, 13х13

# Sample Input 1:
# multiplication_check_list()

# Sample Output 1:
# Правильных результатов: 536
# Неправильных результатов: 7564

# Sample Input 2:
# multiplication_check_list(length_check = False)

# Sample Output 2:
# Правильных результатов: 513
# Неправильных результатов: 7587

# Sample Input 3:
# multiplication_check_list(98, 99)

# Sample Output 3:
# Правильных результатов: 4
# Неправильных результатов: 0

# Sample Input 4:
# multiplication_check_list(98, 99, length_check = False)

# Sample Output 4:
# Правильных результатов: 0
# Неправильных результатов: 4

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

def multiplication_check_list(start=10, stop=99, length_check=True):
    true = 0
    false = 0
    for i in range(start, stop+1):
        for j in range(start, stop+1):
            if i*j == wisdom_multiplication(i, j, length_check):
                true += 1
            else:
                false +=1
    print(*[f'Правильных результатов: {true}', f'Неправильных результатов: {false}'], sep='\n')