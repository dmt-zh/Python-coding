# Дополните ваше предыдущее решение защитой от зависания процесса обработки (или слишком долгого времени выполнения).

# Перепишите функцию main таким образом, чтобы она принимала параметр уставки времени, по завершению которого оставшиеся
# процессы в работе завершались, а ресурсы процесса очищались.

# Функцию main вызывать не надо, только определите ее.



import multiprocessing as mp
from time import sleep

def main(t: int | float) -> None:
    processes = [mp.Process(target=handler, args=(src, )) for src in sources]

    for pr in processes:
        pr.start()

    sleep(t)

    for pr in processes:
        if pr.is_alive():
            pr.kill()
            pr.close()