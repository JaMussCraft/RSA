from utils import modular_exponentiation

# Read in public key (n) from file
with open("public_key.txt", "r") as f:
    n = int(f.readline())

# Read in private key (d) from file
with open("private_key.txt", "r") as f:
    d = int(f.read().strip())

# Read in ciphertext from file
with open("ciphertext.txt", "r") as f:
    ciphertext = int(f.read().strip())

# Decryption: (ciphertext^d) mod n
decrypted_message  = modular_exponentiation(ciphertext, d, n)

# Read in message from file and compare with decrypted
with open("message.txt", "r") as f:
    message = int(f.read().strip())
    print(f"Message and decrypted message  match?: {message == decrypted_message }")

# Write the decrypted message to file
with open("decrypted_message .txt", "w") as f:
    f.write(str(decrypted_message ))
