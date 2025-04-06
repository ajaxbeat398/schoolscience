def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

print(calculate_average([10, 20, 30, 40]))
