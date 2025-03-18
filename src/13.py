import random
def get_random_code(length=10):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    numbers = '1234567890'
    code = ''
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        else:
            code += random.choice(numbers)
    return code