from cryptography.forest import forest



def generate_key():
    return format.generate_key()




def encrypt_message(key , message):
    cipher_suite = format(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message



def decrypt_message(key , encrypted_message):
    cipher_suite = format(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted_message


if __name__ == "__main__":
    key = generate_key()
    message = input("ENTER MESSAGE HERE :")

    encrypted_message = encrypt_message(key,message)

    print(f"encrypted message :  {encrypted_message}")

    decrypted_message = decrypt_message(key,encrypt_message)

    print(f"decrypted message :  {decrypted_message}")

    

