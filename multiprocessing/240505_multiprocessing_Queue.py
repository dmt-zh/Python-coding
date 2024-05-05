# Дана функция обработки: def image_processing(file: str) -> str:

# Функция обрабатывает переданные ей файл и после обработки возвращает лог результата обработки в виде строки.
# Известно, что обработка файла может занимать различное время в зависимости от переданного файла.

# Файлы для обработки необходимо получать из функции генератора get_files. Эта функция возвращает файл (str) для обработки.
# Гарантируется, что генератор возвращает следующий файл для обработки не позднее чем 0.1 секунда после предыдущего запроса.
# В противном случае считаем, что обрабатывать больше нечего и завершаем выполнение всей программы.

# Ваша задача:
# Написать решение, которое выполняет обработку в три раза быстрее однопроцессного решения. 
# Для этого создать и запустить три дочерних процесса обработчика.
# Построить решение в концепции производитель - потребители. Для взаимодействия процессов использовать очередь multiprocessing.Queue.
# В главном процессе сформировать список log_processing в котором должны содержаться все логи обработки файлов.
# В тестирующей системе определены функции image_processing и get_files. Не переопределяйте их, а только вызывайте.


from multiprocessing import Queue, Process
from queue import Empty


def fill_queue(images_to_process):
    for obj in get_files():
        images_to_process.put(obj)

def process_image(input_queue, output_queue):
    while True:
        try:
            img = input_queue.get(timeout=0.3)
            output_queue.put(image_processing(img))
        except Empty:
            break

if __name__ == '__main__':
    input_queue = Queue()
    output_queue = Queue()
    producer = Process(target=fill_queue, args=(input_queue,), daemon=True)
    producer.start()

    consumers = []
    for _ in range(3):
        consumers.append(Process(target=process_image, args=(input_queue, output_queue)))
        consumers[-1].start()
    for consumer in consumers:
        consumer.join()
    
    log_processing = []
    while not output_queue.empty():
        log_processing.append(output_queue.get())