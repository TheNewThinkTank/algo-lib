
from algo_lib.math.fibonacci import fibonacci, fibonacci_generator


def test_fibonacci_zero():
    # Test n = 0
    assert fibonacci(0) == []


def test_fibonacci_one():
    # Test n = 1
    assert fibonacci(1) == [0]


def test_fibonacci_two():
    # Test n = 2
    assert fibonacci(2) == [0, 1]


def test_fibonacci_small_numbers():
    # Test small n values
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_large_n():
    # Test a larger n value
    expected = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
    ]
    assert fibonacci(20) == expected


def test_fibonacci_generator_basic():
    # Test the first 10 Fibonacci numbers from the generator
    fib_gen = fibonacci_generator()
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    generated = [next(fib_gen) for _ in range(10)]
    assert generated == expected


def test_fibonacci_generator_continuity():
    # Ensure the generator continues correctly after multiple calls
    fib_gen = fibonacci_generator()
    for _ in range(10):  # Skip the first 10 numbers
        next(fib_gen)
    next_numbers = [next(fib_gen) for _ in range(5)]
    expected = [55, 89, 144, 233, 377]  # Next numbers in the sequence
    assert next_numbers == expected


def test_consistency_between_functions():
    # Compare the iterative function and generator outputs for a fixed n
    n = 15
    fib_list = fibonacci(n)
    fib_gen = fibonacci_generator()
    fib_gen_list = [next(fib_gen) for _ in range(n)]
    assert fib_list == fib_gen_list


# TODO: fix this test
# def test_fibonacci_generator_large_sequence():
#     # Ensure the generator handles large sequences efficiently
#     fib_gen = fibonacci_generator()
#     for _ in range(1000):  # Skip the first 1000 Fibonacci numbers
#         next(fib_gen)
#     # Check the 1001st Fibonacci number
#     fib_1001 = next(fib_gen)
#     assert fib_1001 == 703303677114228158218352548771835497701812698363
