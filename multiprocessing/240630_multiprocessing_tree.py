# Ваша задача - написать код, который выводит в консоль дерево процессов, начиная от родительского процесса главного процесса программы,
# заканчивая дочерними процессами главного процесса программы.

# Предварительно тестирующая система создаст несколько дочерних процессов, а затем запустит Ваш код, чтобы получилось дерево процессов с
# указанием имени процесса и его идентификатора: <имя процесса>, PID=<идентификатор процесса>.
# Например, если бы тест. система создала два дочерних процесса:

# import multiprocessing
# import os
# import time


# if __name__ == '__main__':
#     multiprocessing.Process(target=time.sleep, args=[2]).start()
#     multiprocessing.Process(target=time.sleep, args=[2]).start()

# То Ваше решение должно вывести в консоль следующее:

# init, PID=10752
#    └─MainProcess, PID=11476
#       ├─Process-2, PID=14672
#       └─Process-1, PID=12548




import multiprocessing as mp
import os

if __name__ == '__main__':
    main_processes =f'init, PID={os.getpid()}\n   └─{mp.current_process().name}, PID={mp.current_process().pid}'
    childer_processes = mp.active_children()
    childer_processes_format = '\n'.join(f'{" "*6}└─{pr.name}, PID={pr.pid}' if pr.name == childer_processes[-1].name else f'{" "*6}├─{pr.name}, PID={pr.pid}' for pr in childer_processes)
    print(main_processes)
    print(childer_processes_format)