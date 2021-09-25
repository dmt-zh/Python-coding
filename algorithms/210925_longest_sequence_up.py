# Задача на программирование: наибольшая последовательнократная подпоследовательность
# Дано целое число 1 ≤ n ≤ 10^3 и массив A[1…n] натуральных чисел, не превосходящих 2 * 10^9.
# Выведите максимальное 1 ≤ k ≤ n, для которого найдётся подпоследовательность 1 ≤ i_1 < i_2 <…<i_k ≤ n длины k,
# в которой каждый элемент делится на предыдущий.

# Sample Input:
# 4
# 3 6 7 12

# Sample Output:
# 3


def longest_sequence_up(arr, n):
    lst = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and lst[j]+1 > lst[i]:
                lst[i] = lst[i]+1
    return max(lst)

n = int(input().strip())
arr = list(map(int, input().split()))
print(longest_sequence_up(arr, n))