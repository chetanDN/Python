import math


def find_area(x, y):
    pi = math.pi
    area = pi * x * y
    print("area of ellipse with semi-major axis of length {} , semi-minor axis of length {} is {}".format(x, y, area))


a = 20  # semi-major axis of length A
b = 10  # semi-minor axis of length B
find_area(a, b)

