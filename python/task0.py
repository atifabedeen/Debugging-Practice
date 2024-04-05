def factorial(n):
    """
    This function calculates the factorial of a number.
    The factorial of a number is the product of all positive integers less than or equal to that number.
    For example, the factorial of 5 is 120.
    """
    result = 1
    for i in range(1, n):
        result *= i
    return result

if __name__ == "__main__":
    result = factorial(5)
    assert result == 120


