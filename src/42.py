import math

def calculate_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

radius = 5.0
height = 10.0
volume = calculate_volume(radius, height)
print("The volume of the cylinder is:", volume)
