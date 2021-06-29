# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

x = float(input())
y = float(input())
operand = str(input())

def calculator(x, y, operand):
    if operand == '+':
        return x + y
    if operand == '-':
        return x - y
    if operand == '/':
        if not y == 0:
            if not x / y == 0:
                return x / y
            return int(x / y)
        return "Деление на 0!"
    if operand == '*':
        return x * y
    if operand == 'mod':
        if not y == 0:
            return x % y
        return "Деление на 0!"
    if operand == 'pow':
        return x ** y
    if operand == 'div':
        if not y == 0:
            return x // y
        return "Деление на 0!"


print(calculator(x, y, operand))