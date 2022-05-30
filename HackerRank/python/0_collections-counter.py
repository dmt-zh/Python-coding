# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x_i amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.

from collections import Counter
x = int(input())
shoe_sizes = Counter(list(map(int, input().split())))

earnings = 0
for _ in range(int(input())):
    size, money = map(int, input().split())
    if size in shoe_sizes and shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        earnings += money

print(earnings)