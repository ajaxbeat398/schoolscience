import random

def create_random_string(length):
    """
    Generates a random string of specified length.
    
    :param length: The desired length of the string.
    :return: A randomly generated string of the given length.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

# Example usage:
random_str = create_random_string(10)
print(random_str)  # Output a random 10-letter alphanumeric string
