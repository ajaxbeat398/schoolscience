import random

def get_random_number(min_value: int, max_value: int) -> int:
    """
    Generates a random integer between min_value and max_value (inclusive).
    
    Parameters:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
        
    Returns:
        int: A randomly generated number within the specified range.
    """
    return random.randint(min_value, max_value)

def main() -> None:
    print("Generating a random integer between 1 and 100.")
    random_number = get_random_number(1, 100)
    print(f"The random number is: {random_number}")

if __name__ == "__main__":
    main()
