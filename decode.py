from cryptography.fernet import Fernet

def decrypt_fernet(ciphertext, key):
    # Crea un objeto Fernet con la clave
    fernet = Fernet(key)

    # Descifra los datos
    plaintext = fernet.decrypt(ciphertext)

    return plaintext

# Ejemplo de uso
key =input("Introduce la llave ->") # Clave secreta generada previamente
key = bytes(key.encode())
# Datos cifrados generados durante el proceso de cifrado con Fernet
ciphertext = input("Introduce el texto cifrado ->")
ciphertext = bytes(ciphertext.encode())

# Descifra los datos

plaintext = decrypt_fernet(ciphertext, key)
print("Datos descifrados:", plaintext)

