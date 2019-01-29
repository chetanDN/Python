import math


class FindArea:
    @staticmethod
    def find_area():
        pi = math.pi
        x = 20
        y = 20
        area = pi * x * y
        print("area of ellipse is :", area)


class Main:
    FindArea.find_area()
