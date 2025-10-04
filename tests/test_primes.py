from math_utils.primes import isprime

def test_isprime_true_cases():
    assert isprime(2)
    assert isprime(3)
    assert isprime(17)
    assert isprime(97)

def test_isprime_false_cases():
    assert not isprime(0)
    assert not isprime(1)
    assert not isprime(9)
    assert not isprime(100)