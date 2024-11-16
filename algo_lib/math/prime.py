
import math


def is_prime(n: int) -> bool:
    """
    Check if a given integer is a prime number.
    
    A prime number is greater than 1 and is divisible only by 1 and itself.

    :param n: Integer to check for primality.
    :type n: int
    :return: True if the number is prime, False otherwise.
    :rtype: bool
    """

    if n <= 1:  # Handle edge cases
        return False
    if n <= 3:  # 2 and 3 are primes
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    
    # Check for factors from 5 onwards, skipping even numbers
    for k in range(5, int(math.sqrt(n)) + 1, 6):
        if n % k == 0 or n % (k + 2) == 0:
            return False
    return True


def generate_primes(limit: int) -> list[int]:
    """
    Generate a list of prime numbers up to a specified limit,
    using the Sieve of Eratosthenes.

    :param limit: The upper limit (inclusive) for generating primes.
    :type limit: int
    :return: A list of prime numbers up to the specified limit.
    :rtype: list[int]
    """

    if limit < 2:
        return []
    
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries as True. An entry will be set to False if it's not a prime.
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime
    
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            # Mark all multiples of the current number as non-prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    # Collect all numbers that are still marked as prime
    return [number for number, prime in enumerate(is_prime) if prime]


def prime_generator():
    """
    Generate an infinite sequence of prime numbers using a segmented sieve.
    
    This approach uses dynamic memory to store known primes and their multiples.

    :yield: The next prime number in the sequence.
    """

    # Dictionary to map composite numbers to their prime factors
    composites = {}
    candidate = 2  # Start with the first prime number

    while True:
        if candidate not in composites:
            # Found a prime number
            yield candidate
            # Mark the first composite number for this prime
            composites[candidate * candidate] = [candidate]
        else:
            # Candidate is composite; update multiples of its factors
            for prime in composites[candidate]:
                composites.setdefault(prime + candidate, []).append(prime)
            del composites[candidate]  # Remove the handled composite

        candidate += 1


def largest_prime_factor(n: int) -> int:
    """
    Find the largest prime factor of the given number.

    :param n: The number to find the largest prime factor for.
    :type n: int
    :return: The largest prime factor of n.
    :rtype: int
    """
    if n <= 1:
        raise ValueError("Number must be greater than 1")

    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1

    # When the loop exits, n itself is the largest prime factor
    return n
