from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(key, password):
    return Fernet(key).encrypt(password.encode())

def decrypt(key, encrypt_password):
    return Fernet(key).decrypt(encrypt_password).decode('utf-8')

password = "passwordtest!@#"
print("[origin password]", password)

key = generate_key()
print("[key]", key)

encrypt_password = encrypt(key, password)
print("[encrypt password]", encrypt_password)

decrypt_password = decrypt(key, encrypt_password)
print("[decrypt password]", decrypt_password)
