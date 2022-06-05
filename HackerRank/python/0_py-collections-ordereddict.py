# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

from collections import OrderedDict

goods = OrderedDict()
n = int(input().strip())
for _ in range(n):
    line = input().strip().split()
    item, price = ' '.join([i for i in line if i.isalpha()]), int(line[-1])
    if item in goods:
        goods[item].append(price)
    else:
        goods[item] = [price]

for k, v in goods.items():
    print(k, sum(v))