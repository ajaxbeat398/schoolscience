import random

def get_random_number(min, max):
    return random.randint(min, max)

def main():
    min = 1
    max = 10
    result = get_random_number(min, max)
    print(result)

if __name__ == "__main__":
    main()
