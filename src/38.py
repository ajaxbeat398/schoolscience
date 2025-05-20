# Random Code Generation Example
import random

def generate_random_code(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    result = ''.join(random.choice(characters) for i in range(length))
    return result

random_code = generate_random_code()
print("Generated Random Code:", random_code)
