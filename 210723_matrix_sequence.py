# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# Sample Input:
# 5

# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

num = int(input())
mtx = [[0 for i in range(num)] for j in range(num)]
cnt = 1
while cnt <= num ** 2:
    for i in range(num):
        for j in range(i, num-i):
            mtx[i][j] = cnt
            cnt += 1
        for j in range(1+i, num-i):
            mtx[j][num-1-i] = cnt
            cnt += 1
        for j in reversed(range(i, num-1-i)):
            mtx[num-1-i][j] = cnt
            cnt += 1
        for j in reversed(range(1+i, num-1-i)):
            mtx[j][i] = cnt
            cnt += 1
for i in mtx:
    print(*i)
