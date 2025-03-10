
import random

def get_random_code():
    """
    Generates a random string of letters and numbers
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    code = ''
    for i in range(10):
        code += random.choice(letters)
        code += random.choice(numbers)
    return code