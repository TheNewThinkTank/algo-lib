
import random
from algo_lib.sampling.reservoir_sample import reservoir_sample


def test_reservoir_sample_basic():
    # Test basic functionality
    data = range(10)
    k = 5
    sample = reservoir_sample(data, k)
    assert len(sample) == k
    assert all(element in data for element in sample)


def test_reservoir_sample_k_equals_n():
    # Test when k equals the size of the generator
    data = range(5)
    k = 5
    sample = reservoir_sample(data, k)
    assert len(sample) == k
    assert sorted(sample) == list(data)


def test_reservoir_sample_k_greater_than_n():
    # Test when k is greater than the size of the generator
    data = range(5)
    k = 10
    sample = reservoir_sample(data, k)
    assert len(sample) == len(data)
    assert sorted(sample) == list(data)


def test_reservoir_sample_empty_generator():
    # Test when the generator is empty
    data = iter([])
    k = 3
    sample = reservoir_sample(data, k)
    assert sample == []


def test_reservoir_sample_randomness():
    # Test randomness by checking multiple samples
    data = range(100)
    k = 10
    random.seed(42)  # Fix seed for reproducibility
    sample1 = reservoir_sample(data, k)
    random.seed(42)
    sample2 = reservoir_sample(data, k)
    assert sample1 == sample2  # Deterministic with the same seed

    # Check that different seeds produce different results
    random.seed(43)
    sample3 = reservoir_sample(data, k)
    assert sample1 != sample3


def test_reservoir_sample_large_data():
    # Test with a large dataset
    data = range(1_000_000)
    k = 1000
    sample = reservoir_sample(data, k)
    assert len(sample) == k
    assert all(isinstance(element, int) for element in sample)
