# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты
# группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
# на этот символ и количество его повторений в этой позиции строки.
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит
# закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.


dna = input()

res = ''
cnt = 1
if len(dna) > 1:
    for i in range(1, len(dna)):
        if dna[i - 1] == dna[i]:
            cnt += 1
        else:
            res += dna[i - 1] + str(cnt)
            cnt = 1
    res += dna[len(dna)-1] + str(cnt)
else:
    res += dna + str(cnt)
print(res)
