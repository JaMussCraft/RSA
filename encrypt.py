from utils import modular_exponentiation

# Read in public key from file
with open("public_key.txt", "r") as f:
    n = int(f.readline())
    e = int(f.readline())

# Read in plaintext message from file
with open("message.txt", "r") as f:
    message = int(f.read().strip())  # The message is a big integer

# Encryption: (message^e) mod n
ciphertext = modular_exponentiation(message, e, n)

# Write the ciphertext to file
with open("ciphertext.txt", "w") as f:
    f.write(str(ciphertext))
