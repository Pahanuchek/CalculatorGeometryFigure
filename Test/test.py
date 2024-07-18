import unittest
from Calculator.calculator import GeometryCalculator


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(GeometryCalculator.circle_area(5), 78.54, places=2)

    def test_triangle_area(self):
        self.assertAlmostEqual(GeometryCalculator.triangle_area(3, 4, 5), 6, places=2)

    def test_right_triangle(self):
        self.assertTrue(GeometryCalculator.right_triangle(3, 4, 5))
