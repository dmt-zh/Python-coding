# Заказчик захотел функционал, позволяющий выявлять незанятость своих таможенных инспекторов. Если инспектор не получает на проверку новую
# таможенную декларацию в течении какого-то времени, об этом следует известить руководство. По результатам таких логов, например, можно 
# оптимизировать кадровый состав.

# К счастью, решение команды построить демонстрационную модель на основе очередей, позволяет довольно просто внедрить этот новый функционал.
# Ваша задача - переписать целевую функцию потребителя так, чтобы в случае неполучения декларации из очереди за установленное время 
# (очередь пуста - работы нет), поток выводил сообщение и завершал свою работу.

# Итак, Ваша задача:

# Переписать вашу целевую функцию с прошлого задания так, чтобы в случае неполучения за заданное время (параметр функции t_wait, тип float) 
# нового объекта - декларации из очереди, выводилось сообщение в формате:
# Empty <datetime> thread = <name>
# где <datetime>- дата и время формирования сообщения (используйте функцию datetime.now() билиотеки datetime)
# <name> - имя потока - потребителя
# например, Empty 2023-05-12 15:00:32.071063 thread = insp_1
# и после этого поток - потребитель завершал свою работу.

# Если же объект получен - то выводить id этого объекта простым принтом.
# (id - идентификационный номер, уникальный код который назначается декларации, соответствует входящему номеру).
# Для демонстрации создайте и запустите один поток-потребитель этой функции с параметром t_wait. Имя потока - потребителя "insp_1".
# Тестирующая система проверяет поведение решение с разными параметрами t_wait. Очереди, декларации, поток - производитель и т.д. реализованы в 
# тестирующей системе под старыми именами. Значение задаваемого параметра t_wait будет определено в тестирующей системе.



import threading
from datetime import datetime

def consumer(t_wait):
    while True:
        try:
            obj = main_queue.get(timeout=t_wait)
            print(obj.id)
            if handler(obj):
                main_queue.task_done()
        except:
            print(f'Empty {datetime.now()} thread = {threading.current_thread().name}')
            break

            
threading.Thread(target=consumer, args=(t_wait,), name='insp_1', daemon=True).start()