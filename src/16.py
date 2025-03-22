import math

def calculate_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

volume = calculate_volume(radius, height)
print(f"The volume is {volume:.2f} cubic units.")
