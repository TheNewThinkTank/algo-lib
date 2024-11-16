

def fibonacci(n: int) -> list[int]:
    """
    Generate the first n Fibonacci numbers.
    
    :param n: Number of Fibonacci numbers to generate.
    :type n: int
    :return: A list of the first n Fibonacci numbers.
    :rtype: list[int]
    """

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence


def fibonacci_generator():
    """
    Generate an infinite sequence of Fibonacci numbers using a generator.
    
    :yield: The next Fibonacci number in the sequence.
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
