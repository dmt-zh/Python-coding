# Ваша задача:
# 1. Измените класс Encrypter согласно новому условию.
# 2. Запустите шифрование для текстовых блоков, которые хранятся в списке text_blocks, по одному дочернему процессу для каждого блока.
# 3. В главном процессе соберите общий результат работы в словарь results, где ключ - это шифр, значение - кортеж:
# (блок текста, результат качества шифрования).
# И выведите results на печать.

# Функция crypto_utils и список text_blocks определены в тестирующей системе, не переопределяйте их, только используйте.
# Тестирующая система проверит время решения и содержание словаря results.

# Внимание! Для решения задачи используйте SharedMemoryManager.


from typing import Callable
from multiprocessing.managers import SharedMemoryManager
from multiprocessing import Process

class Encrypter(Process):
    def __init__(
        self,
        function: Callable | None = None,
        args: tuple[str, SharedMemoryManager.ShareableList, int] | None = None,
    ):
        self.function = function
        self._text = args[0]
        self._sml = args[1]
        self._idx0 = args[-1] * 2
        self._idx1 = args[-1] * 2 + 1
        super().__init__()

    @property
    def cipher(self):
        return self._idx0
    
    @property
    def score(self):
        return self._idx1
    
    @property
    def txt(self):
        return self._text

    def run(self):
        cipher, score = self.function(self._text)
        self._sml[self._idx0] = cipher
        self._sml[self._idx1] = score

def main():
    result_dict, processes = {}, []
    with SharedMemoryManager() as shm_mng:
        shm_list = shm_mng.ShareableList(range(len(text_blocks) * 2))
        for idx, text in enumerate(text_blocks):
            processes.append(Encrypter(function=crypto_utils, args=(text, shm_list, idx)))
            processes[-1].start()
        for process in processes:
            process.join()
        for process in processes:
            cipher = shm_list[process.cipher]
            score = shm_list[process.score]
            result_dict[cipher] = (process.txt, score)
        print(result_dict)

if __name__ == '__main__':
    main()