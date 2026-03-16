def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base Case
    if n <= 1:
        return 1
    
    # Recursive Step & State Change (n - 1)
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    try:
        num = 5
        print(f"The factorial of {num} is: {factorial_recursive(num)}")
        
        # Testing the guard clause
        print(f"Testing negative input: {factorial_recursive(-1)}")
    except ValueError as e:
        print(f"Caught expected error: {e}")