
import math


def is_prime(n: int) -> bool:
    """Check if a given integer is a prime number.

    :param n: _description_
    :type n: int
    :return: _description_
    :rtype: bool
    """
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
