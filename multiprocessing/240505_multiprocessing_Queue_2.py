# Теперь функция генератора файлов для обработки не гарантирует возврата очередного файла за определенный лимит времени,
# могут быть задержки и более 0.1 секунды. Для определения действительного окончания генерации новых файлов для обработки
# функция get_files была изменена. Теперь в качестве последнего элемента она возвращает None. Гарантируется, что генератор
# не зависает навечно и точно вернет None последним элементов после всех файлов для обработки.

# Перепишите Ваше предыдущее решение с учетом этого нового условия. Как и прежде, в тестирующей системе определены функции
# image_processing и get_files. Не переопределяйте их, а только вызывайте.

# Тестирующая система проверяет время Вашего решения и содержание списка log_processing.



from multiprocessing import Queue, Process


def fill_queue(images_to_process):
    for obj in get_files():
        images_to_process.put(obj)

def process_image(input_queue, output_queue):
    while True:
        img = input_queue.get()
        if img is None:
            input_queue.put(None)
            break
        output_queue.put(image_processing(img))


if __name__ == '__main__':
    input_queue = Queue()
    output_queue = Queue()
    producer = Process(target=fill_queue, args=(input_queue,), daemon=True)
    producer.start()

    consumers = []
    for _ in range(3):
        consumers.append(Process(target=process_image, args=(input_queue, output_queue)))
        consumers[-1].start()
    for cnsm in consumers:
        cnsm.join()
    
    log_processing = []
    while not output_queue.empty():
        log_processing.append(output_queue.get())
