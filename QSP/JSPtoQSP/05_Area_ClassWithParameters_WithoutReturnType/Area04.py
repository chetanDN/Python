import math


class FindArea:
    @staticmethod
    def find_area(x, y):
        pi = math.pi
        area = pi * x * y
        print("area of ellipse is :", area)


class Main:
    FindArea.find_area(20, 20)
