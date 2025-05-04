# Write a Java/C/C++/Python program to perform encryption and decryption using the method of the method of Transposition technique.

def encrypt(message, key):
    encrypted = ""
    # Read characters column by column
    for col in range(key):
        pointer = col
        while pointer < len(message):
            encrypted += message[pointer]
            pointer += key
    return encrypted

def decrypt(ciphertext, key):
    num_rows = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        num_rows += 1

    decrypted = [''] * len(ciphertext)
    index = 0

    for col in range(key):
        pointer = col
        while pointer < len(ciphertext):
            decrypted[pointer] = ciphertext[index]
            pointer += key
            index += 1
    return ''.join(decrypted)

# Main program
message = input("Enter message: ").replace(" ", "")
key = int(input("Enter key (number): "))

encrypted_msg = encrypt(message, key)
print("Encrypted:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, key)
print("Decrypted:", decrypted_msg)
