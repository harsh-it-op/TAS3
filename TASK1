def factorial(n):
    """
    Calculate the factorial of a number using iteration.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of the number
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Test the function with sample number 5
sample_number = 5
print(f"The factorial of {sample_number} is {factorial(sample_number)}")
