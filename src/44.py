def sum_of_squares(num1: int, num2: int) -> int:
    """
    This function takes two integers and returns their sum of squares.
    
    Parameters:
    num1 (int): The first integer.
    num2 (int): The second integer.
    
    Returns:
    int: The sum of the squares of num1 and num2.
    """
    return num1 * num1 + num2 * num2

def main():
    # Example usage
    print("The sum of squares of 3 and 4 is:", sum_of_squares(3, 4))

if __name__ == "__main__":
    main()
