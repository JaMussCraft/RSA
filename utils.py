import random


# Computes (base^exponent) mod modulus
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Reduce base modulo first

    while exponent > 0:
        # Multiply result by base if exponent is odd
        if exponent % 2 == 1:
            result = (result * base) % modulus  

        exponent //= 2 # divide exponent by 2 and floor it

        base = (base * base) % modulus  # Square the base each round

    return result


# Fermat Primality Test to check if n is probably prime
# k is the number of random bases to test
def is_probably_prime(n, k=10):
    if n <= 1: # primes have to be > 1
        return False
    
    for _ in range(k):
        a = random.randrange(1, n)  # Pick random base a from [1, n)

        # Cannot be prime
        if modular_exponentiation(a, n - 1, n) != 1: return False  
        
    return True # Could be prime


# Generates a random (probably) prime number with 'digits' many digits
def generate_large_prime(digits=100):
    while True:
        # pick random number with specified num of digits
        candidate = random.randrange(10**(digits - 1), 10**digits)  

        if is_probably_prime(candidate):
            return candidate


# EEA: Returns gcd of (a, b), and integers x, y such that ax + by = gcd(a, b)
def extended_gcd(a, b):
    # Base case
    if b == 0: return a, 1, 0

    # General case
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


# Computes the modular inverse of e mod phi
def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)

    if g != 1:
        raise Exception('Modular inverse does not exist')
    
    return x % phi



