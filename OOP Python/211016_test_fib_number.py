import unittest

class TestFibonacciNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fib_number(0), 0)

    def test_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib_number(n), fib_n)

    def test_positive(self):
        self.assertEqual(fib_number(10), 55)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib_number, -1)
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib_number, -10)

    def test_fractional(self):
        self.assertRaises(ArithmeticError, fib_number, 2.5)

def fib_number(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ArithmeticError
    f_arr = [0, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        f_arr[i] = f_arr[i - 1] + f_arr[i - 2]
    return f_arr[n]

print(fib_number(10))