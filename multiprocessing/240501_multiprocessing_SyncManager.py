# Ваша задача:
# 1. Измените класс Encrypter согласно новому условию.
# 2. Запустите шифрование для текстовых блоков, которые хранятся в списке text_blocks, по одному дочернему процессу для каждого блока.
# 3. В главном процессе соберите общий результат работы в словарь results, где ключ - это шифр, значение - кортеж:
# (блок текста, результат качества шифрования).
# И выведите results на печать.

# Функция crypto_utils и список text_blocks определены в тестирующей системе, не переопределяйте их, только используйте.
# Тестирующая система проверит время решения и содержание словаря results.

# Внимание! Для решения задачи используйте SyncManager.


from typing import Callable
from multiprocessing import Manager
from multiprocessing.managers import SyncManager
from multiprocessing import Process

class Encrypter(Process):
    def __init__(
        self,
        function: Callable | None = None,
        text: str | None = None,
        sync_mng: SyncManager | None = None
    ):
        self.function = function
        self.text = text
        self.sync_mng = sync_mng
        super().__init__()

    def run(self):
        cipher, score = self.function(self.text)
        self.sync_mng[cipher] = (self.text, score)

def main():
    processes = []
    sync_dict = Manager().dict()

    for text in text_blocks:
        processes.append(Encrypter(function=crypto_utils, text=text, sync_mng=sync_dict))
        processes[-1].start()
    for process in processes:
        process.join()

    result_dict = {k: v for k, v in sorted(sync_dict.items())}
    print(result_dict)

if __name__ == '__main__':
    main()