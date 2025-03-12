import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def main():
    print("Enter the minimum value: ")
    min_value = int(input())
    print("Enter the maximum value: ")
    max_value = int(input())
    result = get_random_number(min_value, max_value)
    print(f"The random number is {result}")

if __name__ == "__main__":
    main()
