from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

text = input("Input text for encryption: ")
text_to_bytes = text.encode()

encrypt = f.encrypt(text_to_bytes)
print(f"Encrypted result: {encrypt}")

decrypt = f.decrypt(encrypt)
print(f"Decrypted result: {decrypt}")
print(f"Key for encryption: {key}")

