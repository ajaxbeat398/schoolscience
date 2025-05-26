def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    data = [10, 20, 30, 40]
    print("Average:", calculate_average(data))
except ValueError as e:
    print(e)
