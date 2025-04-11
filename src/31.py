def sum_of_squares(n):
    """
    Calculate the sum of squares of numbers from 1 to n.
    
    Parameters:
        n (int): The upper limit.
        
    Returns:
        int: The sum of squares.
    """
    return sum(i**2 for i in range(1, n+1))

# Example usage
n = 10
result = sum_of_squares(n)
print(f"The sum of squares from 1 to {n} is: {result}")
