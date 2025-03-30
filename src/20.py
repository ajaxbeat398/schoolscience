import math

def calculate_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def main():
    # Example usage: Calculate surface area of a circle with radius 5 and height 10
    radius = 5
    height = 10
    result = calculate_surface_area(radius, height)
    print(f"The surface area is: {result}")

if __name__ == "__main__":
    main()
