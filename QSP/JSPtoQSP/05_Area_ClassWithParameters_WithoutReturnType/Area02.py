class AreaCalculator(object):
    @staticmethod
    def find_area(width, length):
        area_of_rectangle = width * length
        print("area_of_rectangle : ", area_of_rectangle)


class Main:
    AreaCalculator.find_area(10, 20)

