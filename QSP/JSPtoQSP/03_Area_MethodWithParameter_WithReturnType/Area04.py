import math


def find_area(x, y):
    pi = math.pi
    area = pi * x * y
    return area


# a = 20  # semi-major axis of length A
# b = 10  # semi-minor axis of length B
area_of_ellipse = find_area(20, 10)
print("area of ellipse is :", area_of_ellipse)
