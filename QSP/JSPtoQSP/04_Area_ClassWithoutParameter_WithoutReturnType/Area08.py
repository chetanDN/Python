class FindArea:
    @staticmethod
    def area_of_sector():  # angle in radians
        radius = 10
        angle = 30.5
        area_sector = (1 / 2) * radius * radius * angle  # area_of_sector = (angle_of_sector_in degree/360)*pi*r*r (or)
        #  area_of_sector = (angle_of_sector_in_radians/2)*radius*radius (As 360_degree = 2*pi radians)
        print("area of sector is :", area_sector)


class Main:
    FindArea.area_of_sector()
