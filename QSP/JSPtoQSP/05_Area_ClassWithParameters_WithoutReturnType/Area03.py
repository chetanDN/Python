class AreaCalculator(object):
    @staticmethod
    def find_area(x, y, d):
        area_of_trapezoid = ((x + y) / 2) * d  # Area_of_trapezoid
        print("area of trapezoid is :", area_of_trapezoid)


class Main:
    AreaCalculator.find_area(10, 20, 5)
