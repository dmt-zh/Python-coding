# В тестирующей системе задана расчетная функция worker(), которая принимает один единственный аргумент, 
# а возвращает кортеж состоящий их трех значений:
# строка (str), целое число (int), число с плавающей точкой (float).
# При штатном выполнении функция возвращает результат в течении доли секунды, но не исключены и долговременные "зависания".

# Также в тест. системе задана функция генератор get_obj() возвращающая объекты. Ни количество объектов, ни их тип Вам не известны.
# Гарантируется, что объекты поддерживают сериализацию и их количество конечно.

# Вам необходимо написать решение, в котором:
# 1. Используются два процесса: главный и дочерний расчетный процесс, выполняющий функцию worker;
# 2. Для коммуникации между процессами используется канал pipe;
# 3. Главный процесс передает расчетному процессу объекты из генератора и получив результат добавляет его в итоговый список result;
# 4. Выполняется защита от зависания. Если ответ от дочернего процесса превышает 0,3 секунды, процессы необходимо завершить;
# 5. Главный процесс для расчета использует один и тот же дочерний процесс и один и тот же канал, а не создает каждый раз новый для каждого объекта из генератора.

# Тестирующая система проверяет содержимое result (список кортежей из трех значений каждый) и время выполнения программы.


from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection

def process(conn):
    for obj in get_obj():
        result = worker(obj)
        if result is not None:
            conn.send(result)

if __name__ == "__main__":
    result = []
    recv_conn, send_conn = Pipe()
    child_process = Process(target=process, args=[send_conn], daemon=True)
    child_process.start()

    while recv_conn.poll(0.3):
        data = recv_conn.recv()
        result.append(data)