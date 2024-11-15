
import random


def reservoir_sample(generator, k: int):
    """Select k random elements from the generator using reservoir sampling.
    """

    reservoir = []

    for i, element in enumerate(generator):
        if i < k:
            reservoir.append(element)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = element

    return reservoir
