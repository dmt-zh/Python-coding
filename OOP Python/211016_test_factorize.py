import unittest

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in ['string', 1.5]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in [-1, -10, -100]:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        for x in [0, 1]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        for x in [3, 13, 29]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        for x, fact_x in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(i=x):
                self.assertEqual(factorize(x), fact_x)

    def test_many_multipliers(self):
        for x, fact_x in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(i=x):
                self.assertEqual(factorize(x), fact_x)

def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError
    if x < 0:
        raise ValueError
    if x in [0, 1]:
        return (x,)
    if x >= 2:
        factors = []
        for num in range(2, int(x**0.5) + 1):
            while x % num == 0:
                factors.append(num)
                x //= num
        if x != 1:
            factors.append(x)
    return tuple(factors)


# print(factorize(29))

