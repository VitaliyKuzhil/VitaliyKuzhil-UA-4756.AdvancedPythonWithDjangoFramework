import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):
    def __init__(self, message = 'Not valid arguments'):
        super().__init__(message)


class TriangleNotExistException(Exception):
    def __init__(self, message= 'Can`t create triangle with this arguments'):
        super().__init__(message)


class Triangle:
    def __init__(self, sides):
        try:
            if len(sides) == 3:
                try:
                    self.b = float(sides[1]) if isinstance(sides[1], (int, float)) else float([])
                    self.c = float(sides[2]) if isinstance(sides[2], (int, float)) else float([])
                    self.a = float(sides[0]) if isinstance(sides[0], (int, float)) else float([])
                except TypeError:
                    raise TriangleNotValidArgumentException('Not valid arguments')
            else:
                raise TriangleNotValidArgumentException('Not valid arguments')
        except TypeError:
            raise TriangleNotValidArgumentException('Not valid arguments')

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise TriangleNotExistException('Can`t create triangle with this arguments')

        if (sum((self.a, self.b)) <= self.c) or \
                (sum((self.a, self.c)) <= self.b) or \
                (sum((self.b, self.c)) <= self.a):
            raise TriangleNotExistException('Can`t create triangle with this arguments')

    def get_area(self):

        perimeter = (self.a + self.b + self.c) / 2

        area = sqrt(perimeter * (perimeter - self.a) * (perimeter - self.b) * (perimeter - self.c))

        return area



class TriangleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        self.not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        self.not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]


    def test_triangle_area_with_all_valid_test_data(self):

        for parameters, expect in self.valid_test_data:
            with self.subTest(parameters=parameters, expect=expect):
                self.assertAlmostEqual(Triangle(parameters).get_area(), expect, delta=0.5)



    def test_triangle_area_with_not_valid_triangle(self):
        for parameters in self.not_valid_triangle:
            with self.subTest(parameters=parameters):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(parameters).get_area()


    def test_triangle_area_with_not_valid_arguments(self):
        for parameters in self.not_valid_arguments:
            with self.subTest(parameters=parameters):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(parameters).get_area()
