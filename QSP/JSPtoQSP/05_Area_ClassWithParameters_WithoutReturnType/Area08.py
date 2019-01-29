class FindArea:
    @staticmethod
    def area_of_sector(radius, angle):  # angle in radians
        area_sector = (1 / 2) * radius ** 2 * angle  # area_of_sector = (angle_of_sector_in degree/360)*pi*r*r (or)
        #  area_of_sector = (angle_of_sector_in_radians/2)*radius*radius (As 360_degree = 2*pi radians)
        print("area of sector is :", area_sector)


class Main:
    FindArea.area_of_sector(10, 30.5)
