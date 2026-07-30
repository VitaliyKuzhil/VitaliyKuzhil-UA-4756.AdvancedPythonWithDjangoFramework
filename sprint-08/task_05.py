import unittest

def divide(num_1, num_2):
    return float(num_1) / num_2

class DivideTest(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

        with self.assertRaises(ZeroDivisionError):
            divide(9, 0.0)


    def test_with_correct_data_values_and_types(self):

        self.data = [
            ((8, 2), 4.0),
            ((1, 3.0), 0.3333),
            (('5', 2), 2.5),
            ((10.0, 2), 5.0),
            (('5.5', 3), 1.833),
            (('1e-3', 2), 0.0005)
        ]

        places = 2

        for parameters, expect in self.data:
            with self.subTest(parameters=parameters):
                self.assertAlmostEqual(divide(*parameters), expect, places=places)


    def test_with_incorrect_data_values(self):

        self.data = [
            ('f4', 5),
            ('', 2),
            ('25%', 6),
            ('3 000', 7),
            ('gds', 3),
            ('+-1', 5),
            ('3 + 2j', 4)
        ]

        for parameters in self.data:
            with self.subTest(parameters=parameters):
                with self.assertRaises(ValueError):
                    divide(*parameters)


    def test_with_incorrect_data_types(self):

        self.data = [
            (['n'], 7),
            (6, {3: 'three'}),
            (2, (4, 6)),
            ({1, }, 8),
            (8, 'gds'),
            (9, '5.5'),
            (4, '-1'),
            (5 + 3j, 3)
        ]

        for parameters in self.data:
            with self.subTest(parameters=parameters):
                with self.assertRaises(TypeError):
                    divide(*parameters)
