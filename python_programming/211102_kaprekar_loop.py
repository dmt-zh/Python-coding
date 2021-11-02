# Напишите функцию kaprekar_loop(n), которая принимает целое 4х значное число
# (больше 1000, содержащее хотя бы 2 разные цифры), и запускающую "Процесс Капрекара",
# выводящую на печать каждое число цикла с новой строки до тех пор, пока не будет
# получено число 6174 (каждое, включая 6174).


def kaprekar_loop(n):
    print(n)
    num = int(''.join(map(str, sorted(str(n), reverse=True)))) - int(''.join(map(str, sorted(str(n)))))
    while n != 6174:
        return kaprekar_loop(num)