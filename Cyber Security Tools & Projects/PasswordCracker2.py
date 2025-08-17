
import hashlib

def crackhash(inputPass):
    try:
        passFile = open ("wordlist.txt", "r")

    except :
        print("couldnt find the file")

    for password in passFile :
        encPass = Password.encode("UTF-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print ("password found :" + password)

if __name__ == '__main__':
    crackhash("1321111111111hj32g31l2k3jl123f")


    password=admin