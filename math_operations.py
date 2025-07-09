import math

def math_operations():
    """
    Perform various mathematical operations using the math module.
    
    This function:
    1. Takes a number input from user
    2. Calculates square root, natural log, and sine
    3. Displays the results
    """
    try:
        # Get user input
        number = float(input("Enter a number: "))
        
        # Calculate operations
        sqrt_val = math.sqrt(number)
        log_val = math.log(number)
        sin_val = math.sin(number)  # in radians
        
        # Display results
        print(f"\nFor the number {number}:")
        print(f"Square root: {sqrt_val:.4f}")
        print(f"Natural logarithm: {log_val:.4f}")
        print(f"Sine (in radians): {sin_val:.4f}")
        
    except ValueError:
        print("Please enter a valid number.")

# Run the function
math_operations()
