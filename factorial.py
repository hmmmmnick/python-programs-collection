"""
Factorial Calculation in Python
Includes iterative and recursive approaches with input validation.
"""


def factorial_iterative(n: int) -> int:
    """Computes factorial iteratively."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Computes factorial recursively."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number} (Iterative): {factorial_iterative(number)}")
    print(f"Factorial of {number} (Recursive): {factorial_recursive(number)}")