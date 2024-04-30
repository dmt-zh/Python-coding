# Разработчики функции шифрования crypto_utils внесли изменения и теперь функция возвращает кортеж из двух значений:
# 1. уникальная строка длиной 8 символов (здесь без изменений);
# 2. число с плавающей точкой (8 байт) - обобщенное значение отражающее качество выполненного шифрования.

# Ваша задача:
# 1. Измените класс Encrypter согласно новому условию.
# 2. Запустите шифрование для текстовых блоков, которые хранятся в списке text_blocks, по одному дочернему процессу для каждого блока.
# 3. В главном процессе соберите общий результат работы в словарь results, где ключ - это шифр, значение - кортеж:
# (блок текста, результат качества шифрования).
# И выведите results на печать.

# Функция crypto_utils и список text_blocks определены в тестирующей системе, не переопределяйте их, только используйте.
# Тестирующая система проверит время решения и содержание словаря results.

# Внимание! Для решения задачи используйте модуль multiprocessing.shared_memory. Вы можете использовать любой вариант работы с общей памятью.
# Но постарайтесь чтобы Ваше решение использовало память рационально.


from multiprocessing import Process, shared_memory
import struct

class Encrypter(Process):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self._shared_memory = shared_memory.SharedMemory(size=16, create=True)

    def run(self) -> None:
        buffer = self._shared_memory.buf
        cipher, score = crypto_utils(self.text)
        buffer[:8] = cipher.encode()
        buffer[8:16] = struct.pack('d', score)

    @property
    def cipher(self):
        return self._shared_memory.buf[:8].tobytes().decode()

    @property
    def score(self):
        return struct.unpack('d', self._shared_memory.buf[8:16])[0]


def main():
    encrypt_prs = [Encrypter(text=text) for text in text_blocks]
    for pr in encrypt_prs:
        pr.start()
    for pr in encrypt_prs:
        pr.join()

    result = {pr.cipher: (pr.text, pr.score) for pr in encrypt_prs}
    print(result)


if __name__ == '__main__':
    main()