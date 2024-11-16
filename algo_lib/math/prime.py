
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
