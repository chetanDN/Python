import math


def find_area_circle(r1):
    pi = math.pi
    area = pi * r1 * r1  # area of circle
    return area


# r = 10  # radius of circle
area_circle = find_area_circle(10)
print("area of circle :", area_circle)
