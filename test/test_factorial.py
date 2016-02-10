from factorial import factorialClass

fac = factorialClass()

def test_factorial_1_to_10():
    assert fac.calculate(1) == 1
    assert fac.calculate(2) == 2
    assert fac.calculate(3) == 6
    assert fac.calculate(4) == 24
    assert fac.calculate(5) == 120
    assert fac.calculate(6) == 720
    assert fac.calculate(7) == 5040
    assert fac.calculate(8) == 40320
    assert fac.calculate(9) == 362880
    assert fac.calculate(10) == 3628800

def test_factorial_0():
    assert fac.calculate(0) == 1



