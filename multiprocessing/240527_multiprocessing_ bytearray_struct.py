# Известно, что функция crypter шифрует текстовый блок длиной не более 10 символов и возвращает кортеж из двух значений:
# 1 шифр - строка (str) длиной оригинального текстового блока;
# ​2 ​​​​​​служебный параметр шифра - значение с плавающей точкой (float)  длиной 8 байт.

# Ваша задача дописать решение чтобы упорядоченно (слева-направо по содержанию байт массива буфера) вывести данные из буфера в формате:
# text=text; cipher=cipher ; score=score
# где text - текстовый блок для шифрования, cipher - шифр, score - параметр шифра.

# Код сверху, функция crypter, а также список text_blocks, содержащий текстовые блоки для шифрования, заданы в тестирующей системе.


from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection
import struct


def sender(conn: Connection, text: str) -> None:
    text, score = crypter(text[:10])
    data = bytearray(text.encode()) + bytearray(b"\x20" * (10-len(text))) + struct.pack("d", score)
    conn.send_bytes(data)

if __name__ == "__main__":
    _buffer = bytearray(b"\x00" * len(text_blocks) * 18)
    pipes = [Pipe() for _ in range(len(text_blocks))]

    for text, connects in zip(text_blocks, pipes):
        Process(target=sender, args=(connects[0], text)).start()

    for i, connects in enumerate(pipes):
        connects[-1].recv_bytes_into(_buffer, i * 18)

    for n in range(len(text_blocks)):
        start_pos, end_pos = n * 18, (n * 18) + 18
        cipher = _buffer[start_pos:end_pos - 8].decode().strip()
        score = struct.unpack("d", _buffer[end_pos - 8:end_pos])[0]
        print(f'text={text_blocks[n]}; cipher={cipher}; score={score}')
