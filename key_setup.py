from utils import generate_large_prime, mod_inverse

# Generate two large primes with 100 digits
p = generate_large_prime(100)
q = generate_large_prime(100)

# Regenerate if conditions not met
while p == q or abs(p - q) < 10**95:
    q = generate_large_prime(100)

n = p * q
phi = (p - 1) * (q - 1)
e = 65537

# Keep trying next odd number until e and phi are coprime
while phi % e == 0:
    e += 2

# Compute the private exponent d
d = mod_inverse(e, phi)

with open("public_key.txt", "w") as f:
    f.write(f"{n}\n{e}\n")

with open("private_key.txt", "w") as f:
    f.write(f"{d}\n")
