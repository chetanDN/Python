
# class AreaCalculator(object):
#     @classmethod
#     def find_area(cls):
#         b = 10
#         h = 20
#         area_of_triangle = (1 / 2) * b * h
#         print("Area of triangle is :", area_of_triangle)


class AreaCalculator(object):
    @staticmethod
    def find_area():
        b = 11
        h = 20
        area_of_triangle = (1 / 2) * b * h
        print("Area of triangle is :", area_of_triangle)

    # find_area = staticmethod(find_area)


class Main:
    AreaCalculator.find_area()
