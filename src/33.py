def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    y = 1.0
    while True:
        y += (x / y) - y
