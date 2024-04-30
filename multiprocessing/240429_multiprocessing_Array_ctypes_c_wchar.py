# 1. Напишите класс Encrypter, который выполняет целевую функцию crypto_utils в отдельном процессе.
# Функция crypto_utils принимает один аргумент - строковое значение произвольной длины (блок текста). 
# Возвращает шифр - уникальную строку длиной 8 символов.
# 2. Запустите шифрование для текстовых блоков, которые хранятся в списке text_blocks, по одному дочернему процессу для каждого блока.
# 3. В главном процессе соберите общий результат работы в словарь results, где ключ - это шифр, значение - блок текста.
# И выведите results на печать.

# Функция crypto_utils и список text_blocks определены в тестирующей системе, не переопределяйте их, только используйте.
# Тестирующая система проверит время решения и содержание словаря results.


import multiprocessing
import ctypes
from typing import Callable

result = {}

class Encrypter(multiprocessing.Process):
    def __init__(
        self,
        function: Callable | None = None,
        text_to_encrypt: str | None = None
    ) -> None:
        self.func = function
        self.text = text_to_encrypt
        self._result = multiprocessing.Array(ctypes.c_wchar, 8)
        super().__init__()

    @property
    def result(self):
        return self._result[:]

    def run(self) -> None:
        self._result[:] = self.func(self.text)


def main():
    encrypters = []
    for text in text_blocks:
        encrypters.append(Encrypter(function=crypto_utils, text_to_encrypt=text))
        encrypters[-1].start()
    for encrypter in encrypters:
        encrypter.join()
        result[encrypter.result] = encrypter.text
    print(result)


if __name__ == '__main__':
    main()