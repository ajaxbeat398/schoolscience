import math
from random import choice

class RandomNumberGenerator:
    def __init__(self):
        self.random_numbers = []

    def generate_random_number(self):
        while True:
            num = choice(range(1, 101))  # Generate a number between 1 and 100
            if num not in self.random_numbers:  # If the number is not already generated
                return num

# Example usage:
random_generator = RandomNumberGenerator()
print(random_generator.generate_random_number())  # Output might be any random number between 1 and 100
