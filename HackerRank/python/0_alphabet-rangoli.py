# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:
#size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


def print_rangoli(size):
    start = 97
    x = (size * 2 - 1) + (size * 2 - 2)
    letters = [chr(i) for i in range(start, start + size)]

    for i in range(1, size+1):
        lst = letters[::-1][:i-1] + letters[-i:]
        str = '-'.join(lst)
        print(str.center(x, '-'))

    for i in range(size-1, 0, -1):
        lst = letters[::-1][:i-1] + letters[-i:]
        str = '-'.join(lst)
        print(str.center(x, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)