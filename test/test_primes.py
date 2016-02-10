from primes import is_prime

def test_is_0_to_100():
    for index in range(0, 100):
        if index in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
            assert is_prime(index) == True
        else:
            assert is_prime(index) == False

def test_negative_number():
    for index in range(-1, -10, -1):
        assert is_prime(index) == False

