# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
# кодирования повторов, и производит обратную операцию, получая исходный текст.
# Sample Input:
# a3b4c2e10b1

# Sample Output:
# aaabbbbcceeeeeeeeeeb

data = 'E17S11u10U6N17Z8t19x8Z3E11B7H10F19p1M12Y17O18r15w17d1r3c5x18'

res = ''
crt = ''
num = 0

for i in data:
    if i.isalpha():
        res += crt * num
        crt = i
        num = 0
    if i.isdigit():
        num = int(str(num) + i)

res += crt * num
