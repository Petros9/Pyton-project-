from src.basic.point import Point
import unittest


class TestPoint(unittest.TestCase):

    def test_arithmetic(self):
        self.assertEqual(Point(2, 1), Point(2, 1))

        self.assertEqual(Point(2, 3) + Point(3, 14), Point(5, 17))
        self.assertEqual(Point(3, 14) + Point(12, 1), Point(15, 15))

        self.assertFalse(Point(3, 14) + Point(3, 14) == Point(3, 14))
        self.assertFalse(
            Point(2, 3) + Point(12, 1) == Point(15, 15) + Point(5, 17))

        self.assertEqual(Point(-1, -1), -Point(1, 1))
        self.assertEqual(Point(12, -5), -Point(-12, 5))

    def test_integral(self):
        p1 = Point(1, 2)

        p1 += Point(3, 14)
        p1.x = 12
        p1 = p1 - Point(3, 5)
        p1.y = -7
        p1 = p1 + p1 + p1
        p1 = -p1
        p1 -= Point(1, 2)

        self.assertEqual(p1, Point(-28, 19))


if (__name__ == "__main__"):
    unittest.main()
