# Вы получили доступ к секретному чату с более чем 200 участниками. В чате часто дарят ключи от Windows 7.
# Вы выкачали все сообщения от новых к старым и проходите по ним программой. Нужные ключи в чате всегда
# отправляют в виде: Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
# Где X - любая буква от A до Z, или любая цифра. Перед нужным ключом должна быть строка Activation key: .

# Вот примеры ключей активации:
# YDMGR-MYQ3R-4XKRK-VHPDK-H7BY2
# GXRHM-CGB6Y-4WRD9-KFD7C-QXQ2B
# C7KYW-CBKVC-DPC82-7TPKD-Y8T2C
# BQXR3-84D93-G2RK7-HDKH2-X938C
# BR3DD-WJ2D6-RM84G-BHWQK-WFHW3
# H7RRB-QPCYB-BMHYY-KB2YV-T8YYW

# Программа получает 5 строк и должна вывести ключ. Гарантируется, что в этих строках есть как минимум 1 ключ!
# Вы должны найти первый ключ, который вам попадётся, и вывести его на экран. Выводить нужно сам ключ!

# Sample Input 2:
# Would you care for1 a cup of tea?
# Only if you’re having one.
# CM0T1-6W7ZJ-XY0Z3-ZROM3-BDLZ9
# Yeah I have one and I have one Activation key: BR3DD-WJ2D6-RM84G-BHWQK-WFHW3
# Do you take milk and sugar?

# Sample Output 2:
# BR3DD-WJ2D6-RM84G-BHWQK-WFHW3



import sys
import re

data = list(map(str.strip, sys.stdin.readlines()))

def windows_key_finder(data):
    pattern = r'(?<=Activation key:)\s?(?:[A-Z\d]{5}-){4}[A-Z\d]{5}'
    raw_keys = list(filter(lambda x: re.search(pattern, x), data))
    key = re.search(pattern, raw_keys[-1]).group().strip()
    return key

print(windows_key_finder(data))