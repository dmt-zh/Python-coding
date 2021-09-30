# Задача на программирование повышенной сложности: наибольшая невозрастающая подпоследовательность
#  Дано целое число 1 ≤ n ≤ 10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
#  Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину k, во второй — её
#  индексы 1 ≤ i_1 <i_2 <…< i_k ≤n (таким образом, A[i_1] ≥ A[i_2] ≥ ... ≥ A[i_n]).

def negative_sequence(n, arr):
    inf = float('inf')
    lst = [inf] + [-inf] * (n+1)
    sequence = []
    res = []

    for i in range(n):
        left = 0
        right = n + 1
        while left+1 < right:
            mid = (left + right)//2
            if lst[mid] >= arr[i]:
                left = mid
            else:
                right = mid
        lst[right] = arr[i]
        sequence.append([right, i])

    lst = [i for i in lst if i != inf and i != -inf]
    cnt = len(lst)

    while cnt > 0:
        for elem in sequence[::-1]:
            if elem[0] == cnt:
                res.append(elem[1]+1)
                cnt -= 1

    return res[::-1]

n = int(input().strip())
arr = list(map(int, input().split()))

ans = negative_sequence(n, arr)

print(len(ans))
print(*ans)
