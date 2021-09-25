# Задача на программирование: расстояние редактирования
# Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
# содержащих строчные буквы латинского алфавита.

# Sample Input 1:
# ab
# ab
# Sample Output 1:
# 0

# Sample Input 2:
# short
# ports
# Sample Output
# 3

def edit_dist_bu(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    mtx = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(n + 1):
        mtx[0][i] = i
    for j in range(m + 1):
        mtx[j][0] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diff = 1 if arr1[j - 1] != arr2[i - 1] else 0
            mtx[i][j] = min(mtx[i][j - 1] + 1, mtx[i - 1][j] + 1, mtx[i - 1][j - 1] + diff)

    return mtx[m][n]


print(edit_dist_bu(input(), input()))