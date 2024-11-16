
import pytest
from algo_lib.math.prime import (
    is_prime,
    generate_primes,
    prime_generator,
    largest_prime_factor
    )


def test_is_prime_edge_cases():
    # Edge cases: numbers less than 2 are not prime
    assert not is_prime(-1)
    assert not is_prime(0)
    assert not is_prime(1)


def test_is_prime_small_primes():
    # Small prime numbers
    assert is_prime(2)
    assert is_prime(3)


def test_is_prime_small_non_primes():
    # Small non-prime numbers
    assert not is_prime(4)
    assert not is_prime(9)
    assert not is_prime(10)


def test_is_prime_large_primes():
    # Large prime numbers
    assert is_prime(29)
    assert is_prime(97)
    assert is_prime(104729)  # A known prime


def test_is_prime_large_non_primes():
    # Large non-prime numbers
    assert not is_prime(100)
    assert not is_prime(104728)  # 104729 - 1
    assert not is_prime(123456)


def test_is_prime_special_cases():
    # Edge case for even and odd non-primes
    assert not is_prime(25)  # Odd non-prime
    assert not is_prime(28)  # Even non-prime


def test_generate_primes_empty():
    # Test edge case where no primes are possible
    assert generate_primes(1) == []
    assert generate_primes(0) == []
    assert generate_primes(-10) == []


def test_generate_primes_small_numbers():
    # Test small numbers
    assert generate_primes(10) == [2, 3, 5, 7]
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_generate_primes_large_numbers():
    # Test a larger range
    assert generate_primes(50) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
        ]


def test_generate_primes_single_prime():
    # Test ranges containing only one prime
    assert generate_primes(2) == [2]
    assert generate_primes(3) == [2, 3]


def test_prime_generator():
    # Test the first 10 primes using the generator
    prime_gen = prime_generator()
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for expected in expected_primes:
        assert next(prime_gen) == expected


def test_prime_generator_matches_generate_primes():
    # Compare the output of the generator to the list of primes
    prime_gen = prime_generator()
    limit = 100
    primes_from_generator = [
        next(prime_gen) for _ in range(len(generate_primes(limit)))
        ]
    primes_from_list = generate_primes(limit)
    assert primes_from_generator == primes_from_list


def test_prime_generator_continues_correctly():
    # Ensure the generator continues generating primes correctly
    prime_gen = prime_generator()
    # Skip the first 20 primes
    for _ in range(20):
        next(prime_gen)
    # Check the next primes
    next_primes = [next(prime_gen) for _ in range(5)]
    expected_primes = [73, 79, 83, 89, 97]  # 21st to 25th primes
    assert next_primes == expected_primes


def test_largest_prime_factor_small_numbers():
    # Small numbers with known largest prime factors
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(5) == 5
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(15) == 5


def test_largest_prime_factor_large_number():
    # Known large number
    assert largest_prime_factor(600851475143) == 6857


def test_largest_prime_factor_prime_number():
    # A prime number should return itself
    assert largest_prime_factor(97) == 97
    assert largest_prime_factor(131) == 131


def test_largest_prime_factor_edge_cases():
    # Edge cases
    with pytest.raises(ValueError):
        largest_prime_factor(1)  # No prime factors
    with pytest.raises(ValueError):
        largest_prime_factor(0)  # No prime factors
    with pytest.raises(ValueError):
        largest_prime_factor(-10)  # Negative numbers have no valid prime factors


def test_largest_prime_factor_composite_numbers():
    # Composite numbers
    assert largest_prime_factor(48) == 3  # 2 * 2 * 2 * 2 * 3
    assert largest_prime_factor(100) == 5  # 2 * 2 * 5 * 5
