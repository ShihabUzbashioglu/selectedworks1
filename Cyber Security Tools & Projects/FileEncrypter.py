







def generate_key():
    return format.generate_key()

def save_key(key , key_file):
    with open(key_file,'wb') as file:
        file.write(Key)

def load_key(key_file):
    with open(key_file,'rb') as file:
        return file.read()
    
#encrypt a file

def encrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        
        data = file.read()

    format = format(key)
    encrypted_data = format.encrypt(data)


    with open(output_file,'wb') as file:
        file.write(encrypted_data)


def decrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        encrypted_data = file.read()


    format = format(key)

    decrypted_data =format.decrypt(encrypted_data)

    with open(output_file,'wb') as file:
        file.write(encrypted_data)



if __NAME__ == '__main__':
    key = generate_key()
    key_file = 'decryption_key.key'
    save_key(key , key_file)

    input_file = 'plain_text.txt'
    encrypted_file = 'encrypted_file.txt'
    decrypted_file = 'decrypted_file.txt'

    encrypt_file(input_file , encrypted_file , key)

    print(f'file : {input_file}  encrypted is : {encrypt_file}')

    
    decrypt_file(encrypted_file , decrypted_file , key)

        print(f'file : {encrypted_file}  encrypted is : {decrypted_file}')

    

