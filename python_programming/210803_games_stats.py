# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
# выводит на стандартный вывод сводную таблицу результатов всех матчей.За победу команде начисляется 3 очка,
# за поражение — 0, за ничью — 1. Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Порядок вывода команд произвольный.

# Sample Input
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


table = []
for game in range(int(input())):
    game = str(input()).split(';')
    table.append(game)

d = {}

for i in range(len(table)):
    for j in range(len(table[0])):
        if j % 2 == 0:
            k = table[i][j]
        if k not in d:
            d[k] = [0, 0, 0, 0, 0]
        if j % 2 == 1:
            if j - 1 == 0:
                scr1 = int(table[i][j])
            elif j - 3 == 0:
                scr2 = int(table[i][j])
                if scr1 > scr2:
                    d[table[i][0]][1] = d[table[i][0]][1] + 1
                    d[table[i][0]][4] = d[table[i][0]][4] + 3
                    d[table[i][2]][3] = d[table[i][2]][3] + 1
                elif scr1 == scr2:
                    d[table[i][0]][2] = d[table[i][0]][2] + 1
                    d[table[i][0]][4] = d[table[i][0]][4] + 1
                    d[table[i][2]][2] = d[table[i][2]][2] + 1
                    d[table[i][2]][4] = d[table[i][2]][4] + 1
                else:
                    d[table[i][2]][1] = d[table[i][2]][1] + 1
                    d[table[i][2]][4] = d[table[i][2]][4] + 3
                    d[table[i][0]][3] = d[table[i][0]][3] + 1
            if k in d:
                d[k][0] = d[k][0] + 1

for k, v in d.items():
    print((k+':'), *v, end='\n')