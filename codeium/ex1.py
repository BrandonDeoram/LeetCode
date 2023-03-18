# Write me a function that returns true if a number is prime and false if it is not prime.


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

