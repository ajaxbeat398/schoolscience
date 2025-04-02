import math

def calculate_volume(cylinder_radius: float, cylinder_height: float) -> float:
    """
    Calculate the volume of a cylinder.
    
    Parameters:
        cylinder_radius (float): The radius of the cylinder's base.
        cylinder_height (float): The height of the cylinder.
        
    Returns:
        float: The volume of the cylinder.
    """
    return math.pi * cylinder_radius ** 2 * cylinder_height

if __name__ == "__main__":
    # Example usage
    print("The volume of a cylinder with radius 3 and height 5 is:", calculate_volume(3, 5))
