# You have to generate a list of the first N fibonacci numbers, 0 being the first number.
# Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

# Sample Input
# 5

# Sample Output
# [0, 1, 1, 8, 27]

cube = lambda x: x ** 3

def fibonacci(n):
    if n > 0:
        arr = [0]
        prev, cur = 0, 1
        for i in range(1, n):
            prev, cur = cur, prev + cur
            arr.append(prev)
        return arr
    else:
        return []

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))