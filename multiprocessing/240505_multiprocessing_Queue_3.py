# Решите задачу кодирования используя очередь как удобное средство получение результатов. 
# Только в этот раз ничего не печатайте, только соберите общий результат работы в словарь results,
# где ключ - это шифр, значение - кортеж: (блок текста, результат качества шифрования).

# Система тестирования проверит время решения и содержание словаря results.


from multiprocessing import Queue, Process


def process_txt(text, output_queue):
    chyper, score = crypto_utils(text)
    packed = {chyper: (text, score)}
    output_queue.put(packed)

if __name__ == '__main__':
    output_queue = Queue()
    consumers = []
    for text in text_blocks:
        consumers.append(Process(target=process_txt, args=(text, output_queue)))
        consumers[-1].start()
    for cnsm in consumers:
        cnsm.join()
    
    results = {}
    while not output_queue.empty():
        results.update(output_queue.get())