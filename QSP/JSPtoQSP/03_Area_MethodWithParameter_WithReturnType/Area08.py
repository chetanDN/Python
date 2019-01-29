def area_of_sector(radius, angle):  # angle in radians
    area = (1 / 2) * radius * radius * angle  # area_of_sector = (angle_of_sector_in degree/360)*pi*r*r (or)
    #  area_of_sector = (angle_of_sector_in_radians/2)*radius*radius (As 360_degree = 2*pi radians)
    return area


# r = 10  # radius of sector
# theta = 30.5  # angle in radians
area_sector = area_of_sector(10, 30.5)
print("area of sector is :", area_sector)
