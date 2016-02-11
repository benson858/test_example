#
# https://www.jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
# https://docs.python.org/2.7/library/unittest.html
#
#   python -m unittest discover
#


def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


class primeNumberClass():
    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def nextPrime(self, number):
        index = number + 1
        while not self.isPrime(index):
            index += 1
        return index


