# Симуляция обработки сетевых пакетов.
# Реализовать обработчик сетевых пакетов.
# Вход. Размер буфера size и число пакетов n, а так-же две последовательности arrival1 , . . . , arrival_n и
# duration1 , . . . , duration_n, обозначающих время поступления и длительность обработки n пакетов.
# Выход. Для каждого из данных n пакетов необходимо вывести время начала его обработки или − 1, если пакет
# не был обработан (это происходит в случае, когда пакет поступает в момент, когда в буфере компьютера уже
# находится size пакетов).

# Ваша цель — реализовать симу лятор обработки сетевых пакетов. Для i-го пакета известно время его поступления
# arrival_i, а также время duration_i, необходимое на его обработку. В вашем распоряжении имеется один процессор,
# который обрабатывает пакеты в порядке их поступления. Если процессор начинает обрабатывать пакет i (что занимает
# время duration_i), он не прерывается и не останавливается до тех пор, пока не обработает пакет.

# Sample Input 1:
# 1 0
# Sample Output 1:


# Sample Input 2:
# 1 1
# 0 0
# Sample Output 2:
# 0

# Sample Input 3:
# 1 1
# 0 1

# Sample Output 3:
# 0

buffer, num = list(map(int, input().split()))

stack = []
timing = []

for package in range(num):
    t_arv, t_dur = map(int, input().split())

    if len(stack) < buffer:
        if len(stack) == 0:
            timing.append(t_arv)
            stack.append(t_arv + t_dur)
        else:
            timing.append(max(t_arv, stack[-1]))
            stack.append(max(t_arv, stack[-1] + t_dur))
    else:
        if t_arv >= stack[0]:
            timing.append(max(t_arv, stack[-1]))
            stack.append(max(t_arv, stack[-1]) + t_dur)
            stack.pop(0)
        else:
            timing.append(-1)

print(*timing, sep='\n')