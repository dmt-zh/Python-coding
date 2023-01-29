# Напишите программу, которая посимвольно скопирует содержимое файла in.txt в файл out.txt.
# За раз нужно считывать символов столько, чтобы оперативная память не страдала, к примеру 65536.


BLOCK_SIZE = 65536

with open('in.txt', encoding='utf8') as fin, open('out.txt', 'w') as fout:
    while data := fin.read(BLOCK_SIZE):
        fout.write(data)