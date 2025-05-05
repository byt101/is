import math

# Function to check if a number is prime
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

# Generate RSA keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e (public exponent)
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2  # Try next odd number

    # Find d (private exponent)
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt text message
def encrypt(public_key, message):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt text message
def decrypt(private_key, encrypted_message):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])

# Main program
print("Simple RSA Encryption/Decryption")
p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

# Generate keys
public_key, private_key = generate_keys(p, q)

print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

message = input("Enter a message to encrypt: ")

# Encrypt and Decrypt
encrypted_message = encrypt(public_key, message)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:", decrypted_message)


# I/P : 17, 11, hi/hello

# Formula :

# Encryption
# C = (P ^ e) mod n

# Decryption
# P = (C ^ d) mod n


# n = p × q --To calculate n
# phi = (p - 1) × (q - 1) --To calculate phi
# (d × e) mod phi = 1 --To calculate d 
