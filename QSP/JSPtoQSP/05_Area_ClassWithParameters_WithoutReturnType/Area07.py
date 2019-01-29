import math

class FindArea:
    @staticmethod
    def find_area_circle(r1):
        pi = math.pi
        area_circle = pi * r1 * r1  # area of circle
        print("area of circle :", area_circle)


class Main:
    FindArea.find_area_circle(10)
