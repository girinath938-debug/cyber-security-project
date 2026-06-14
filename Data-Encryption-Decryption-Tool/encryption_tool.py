# Data Encryption and Decryption Tool
# Using Caesar Cipher Technique

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26

            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
message = input("Enter a message: ")
shift_key = int(input("Enter shift key: "))

encrypted = encrypt(message, shift_key)
print("\nEncrypted Message:", encrypted)

decrypted = decrypt(encrypted, shift_key)
print("Decrypted Message:", decrypted)
