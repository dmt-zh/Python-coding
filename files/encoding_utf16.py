# Напишите программу, которая достанет содержимое в кодировке cp1252 из бинарного файла
# file.bin и запишет результат в result.txt в кодировке UTF-16.


with open('file.bin', 'rb') as fin, open('result.txt', 'w', encoding='utf-16') as fout:
    fout.write(fin.read().decode('cp1252'))