
import random
def roll_dice(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 6))
    return result