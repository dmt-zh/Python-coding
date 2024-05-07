# Простое задание на применение базовых методов получения и отправки.

# Допишите код, передав через канал 4 объекта: строку, целое число, число с плавающей точкой и bytearray,
# который содержит закодированную упаковку строки и целого числа. В главном процессе получите объекты и
# соберите их в список recv_data в порядке их отправки.

# При использовании в решении .to_bytes длина для целого числа - 4 байта, порядок byteorder = "big"


from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def sender(conn: Connection) -> None:
    message = "Hello from sender!"
    number = 42
    float_number = 3.14159
    b_arr = bytearray(message.encode()) + bytearray(number.to_bytes(4, byteorder='big'))
    with conn:
        conn.send(message)
        conn.send(number)
        conn.send(float_number)
        conn.send_bytes(b_arr)


if __name__ == "__main__":
    recv_data = []
    recv_conn, send_conn = Pipe(duplex=False)
    Process(target=sender, args=[send_conn]).start()
    with recv_conn:
        for _ in range(3):
            recv_data.append(recv_conn.recv())
        recv_data.append(recv_conn.recv_bytes())