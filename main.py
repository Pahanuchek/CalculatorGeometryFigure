import unittest

from Calculator.calculator import GeometryCalculator


def main():
    # Пример использования калькулятора площадей геометрических фигур
    radius = 5
    side_1 = 3
    side_2 = 4
    side_3 = 5

    print("Площадь круга:", GeometryCalculator.circle_area(radius))
    print("Площадь треугольника:", GeometryCalculator.triangle_area(side_1, side_2, side_3))
    print("Является ли треугольник прямоугольным?", GeometryCalculator.right_triangle(side_1, side_2, side_3))

    # Пример использования юнит-тестов
    unittest.main()


if __name__ == "__main__":
    main()
