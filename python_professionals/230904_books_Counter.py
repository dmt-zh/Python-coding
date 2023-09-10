# Тимур продает книги по математике за 1—11 класс. У него есть список, в котором указаны все книги,
# имеющиеся в наличии. К Тимуру приходят n покупателей, называют номер класса, за который они хотят приобрести книгу,
# и сумму, которую они готовы заплатить, и если книга есть в наличии, Тимур ее продает.

# Напишите программу, которая вычисляет общую сумму денег, которую Тимур заработает на продаже книг.

# Формат входных данных
# На вход программе в первой строке подается последовательность чисел, разделенных пробелом, представляющих набор книг,
# которые имеются в наличии. Каждое число последовательности — книга за указанный класс, например, последовательность 1 1 4
# представляет набор из двух книг за первый класс и одной книги за четвертый класс. Вторая строка содержит число n — количество
# покупателей. В последующих n строках вводятся два числа, разделенные пробелом, где первое число является номером класса,
# второе — суммой, предлагаемой покупателем.

# Формат выходных данных
# Программа должна вывести единственное число — общую сумму денег, которую заработал Тимур.

# Sample Input 1:
# 1 1 11 9 5 5 7 9 9
# 7
# 1 300
# 1 250
# 11 400
# 1 300
# 7 200
# 9 400
# 7 250

# Sample Output 1:
# 1550



import sys
from collections import Counter


total_sum = 0

books, n, *buyers = list(map(str.strip, sys.stdin.readlines()))
books_for_sale = Counter(map(int, books.split()))

for bueyr in buyers:
    class_, price = list(map(int, bueyr.split()))
    total_sum += price * bool(books_for_sale[class_])
    books_for_sale -= Counter({class_: 1})

print(total_sum)