# Таможенное управление в среднем может проверить 30 грузовых таможенных деклараций за рабочий день если все инспекторы работают в обычном темпе
# Но дни бывают разные. Например, в предпраздничные дни количество деклараций увеличивается. Если часть деклараций остается необработанной, 
# оставшиеся декларации будут обработаны в следующий менее нагруженный рабочий день.

# Вам нужно создать две очереди: рабочая (основная) очередь деклараций с именем main_queue с ограничением размера в 30 деклараций и 
# вспомогательная очередь "работы на завтра" с именем sup_queue.

# Пока команда дорабатывает сервис передачи таможенных деклараций, включая валидацию деклараций, вам поручили написать и протестировать
# основную логику взаимодействия программы.

# Кроме двух очередей Вам нужно:

# Определить целевую функцию производителя. Эта простая функция всего лишь добавляет декларацию (экземпляры класса CCD) в основную очередь,
# если она не заполнена. А если заполнена - то добавление происходит в вспомогательную очередь. Сервис доставки деклараций еще не готов, 
# поэтому для тестов Вам подготовили так называемую mock функцию, имитирующую доставку информаций о грузе (а фактически генератор фейковых, 
# но валидных словарей для создания экземпляров класса CCD). Функция get_next_declar() является таким генератором. Ваша функция производителя должна
# работать в цикле, пока возвращаемый объект генератора не будет None.

# Определить целевую функцию потребителя. Эта функция всего лишь получает декларацию из основной очереди, обарабатывает ее и после завершения помечает
# как обработанную. Функция обработки тоже еще не готова, поэтому в качестве обработки для каждого экземпляра CCD полученного из очереди, нужно вызвать
# функцию handler() и передать в нее декларацию в качестве аргумента. После успешной обработки, handler() вернет True, после чего задачу нужно пометить выполненной.
# Вашу функцию потребителя запустите в бесконечном цикле.

# Запустите один поток - производитель с именем "prod_0". В основном потоке программы дождитесь завершения работы потока - производителя.

# Запустите три потока - инспектора, с соответствующими именами (атрибуты .name): "insp_1", "insp_2", "insp_3". Потоки - инспекторы запустите в демоническом режиме.

# В основном потоке программы дождитесь завершения обработки всех задач потоками - инспекторами а затем переместите все декларации из второстепенной очереди в основную.

# В тестирующей системе уже определен класс CCD из прошлой задачи, функции get_next_declar и handler. Система проверяет время выполнения программы, 
# итоговое содержание и очередность деклараций в очередях.


import queue
import threading

main_queue = queue.PriorityQueue(30)
sup_queue = queue.PriorityQueue()

def producer():
    for obj in get_next_declar():
        item = CCD(obj)
        if not main_queue.full():
            main_queue.put(item)
        else:
            sup_queue.put(item)

def consumer():
    while not main_queue.empty():
        obj = main_queue.get()
        if handler(obj):
            main_queue.task_done()

prod_0 = threading.Thread(target=producer, name='prod_0')
prod_0.start()
prod_0.join()

workers = [
    threading.Thread(target=consumer, name='insp_1', daemon=True),
    threading.Thread(target=consumer, name='insp_2', daemon=True),
    threading.Thread(target=consumer, name='insp_3', daemon=True)
]

for thr in workers:
    thr.start()

main_queue.join()

while not sup_queue.empty():
    main_queue.put(sup_queue.get())