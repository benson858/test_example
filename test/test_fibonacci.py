from fibonacci import fibonacciClass

fib = fibonacciClass()

def test_fibonacci_0():
    assert fib.calculate(0) == 0

def test_fibonacci_1_to_10():
    assert fib.calculate(1) == 1
    assert fib.calculate(2) == 1
    assert fib.calculate(3) == 2
    assert fib.calculate(4) == 3
    assert fib.calculate(5) == 5
    assert fib.calculate(6) == 8
    assert fib.calculate(7) == 13
    assert fib.calculate(8) == 21
    assert fib.calculate(9) == 34
    assert fib.calculate(10) == 55

def test_negative_number():
    for index in range(-1, -10, -1):
        assert fib.calculate(index) == 0

