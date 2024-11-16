
from algo_lib.math.prime import is_prime


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
