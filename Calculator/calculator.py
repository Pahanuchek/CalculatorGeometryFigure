import math


class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side_1, side_2, side_3):
        s = (side_1 + side_2 + side_3) / 2
        return math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

    @staticmethod
    def right_triangle(side_1, side_2, side_3):
        sides = [side_1, side_2, side_3]
        max_side = max(sides)
        sides.remove(max_side)
        return math.isclose(max_side ** 2, sides[0] ** 2 + sides[1] ** 2)
