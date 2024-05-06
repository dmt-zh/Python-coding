# Использование очереди JoinableQueue отлично вписывается в решения с концепцией производители - потребители.
# Перепишите решение позапрошлой задачи. В условиях изменилось только одно: гарантируется, что функция 
# генератор "не зависает", допустимо даже длительное ожидание более 0,1 секунды.

# Напишите решение без всяких таймаутов, ожиданий выполнения потоков потребителей (join() процессов - потребителей)
# и прочим не нужным в случае использования JoinableQueue.

# А для получения результата используйте простую очередь SimpleQueue.



from multiprocessing import JoinableQueue, Process, SimpleQueue

input_queue = JoinableQueue()
output_queue = SimpleQueue()

def fill_queue(images_to_process):
    for obj in get_files():
        images_to_process.put(obj)

def process_image(input_queue, output_queue):
    while True:
        img = input_queue.get()
        output_queue.put(image_processing(img))
        input_queue.task_done()

if __name__ == '__main__':
    producer = Process(target=fill_queue, args=(input_queue,))
    producer.start()

    consumers = []
    for _ in range(3):
        consumers.append(Process(target=process_image, args=(input_queue, output_queue), daemon=True))
        consumers[-1].start()

    producer.join()
    input_queue.join()
    log_processing = []

    while not output_queue.empty():
        log_processing.append(output_queue.get())