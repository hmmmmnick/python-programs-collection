"""
Fibonacci Series Generator in Python
Generates n terms of the Fibonacci sequence.
"""


def generate_fibonacci(n_terms: int) -> list:
    """Generates the first n terms of the Fibonacci sequence."""
    if not isinstance(n_terms, int) or n_terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")

    if n_terms == 1:
        return [0]

    series = [0, 1]
    while len(series) < n_terms:
        series.append(series[-1] + series[-2])
    return series


if __name__ == "__main__":
    terms = 10
    print(f"First {terms} Fibonacci numbers: {generate_fibonacci(terms)}")