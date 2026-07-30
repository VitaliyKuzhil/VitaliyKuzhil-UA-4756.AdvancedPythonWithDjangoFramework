import unittest
from math import sqrt


def quadratic_equation(a, b, c):

    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        raise ValueError

    d = b ** 2 - 4 * a * c

    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        return x2, x1



class QuadraticEquationTest(unittest.TestCase):

    def test_quadratic_equation_with_two_rel_roots(self): # (D > 0)

        places = 4

        x1, x2 = quadratic_equation(2, 1, -1)
        self.assertAlmostEqual(x1, 0.5, places=places)
        self.assertAlmostEqual(x2, -1.0, places=places)

        x1, x2 = quadratic_equation(1, 5, 6)
        self.assertAlmostEqual(x1, -2.0, places=places)
        self.assertAlmostEqual(x2, -3.0, places=places)

    def test_quadratic_equation_with_one_rel_root(self): # (D = 0)
        self.assertAlmostEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_quadratic_equation_with_any_rel_roots(self): # (D < 0)
        self.assertAlmostEqual(quadratic_equation(4, 1, 2), None)

    def test_quadratic_equation_with_error_condition(self): # (a = 0)
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)
