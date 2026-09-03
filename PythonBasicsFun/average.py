import random
import pytest

def compute_average(values):
    # TODO: fix this
    return -1.0

# pytest executes functions/methods as tests that start with "test_"
def test_compute_average():
    values = [0, 1, 2, 3]
    assert compute_average(values) == 1.5

    random.seed(0) # for reproducibility
    values = [random.randint(0, 100) for _ in range(10)]
    assert compute_average(values) == 55.3

def main():
    # TODO: write your own code to call compute_average()
    pass

if __name__ == "__main__":
    main()