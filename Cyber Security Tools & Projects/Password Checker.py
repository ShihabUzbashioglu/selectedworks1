import math
import string

COMMON_PASSWORDS = ['12345','PASSWORD','ADMIN','RELO2345','JOHNT3456']


def  calculate_entropy(password:str)->float:
    charset = 0
    if any(c.islower() for c in password):
        charset +=26
    if any(c.isdigit() for c in password):
        charset +=26
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    if any(c.isupper() for c in password):
        charset +=26
    if any(c.isspace() for c in password):
        charset +=1

    if charset==0:
        return 0
    
    entropy = len(password) + math.log2(charset)
    return round(entropy ,2)



def score_password(password:str)->float:
    score = 0
    length = len(password)
    entropy = calculate_entropy(password)


    if length >=8:
        score +=20
    if length >=12:
        score +=10
    if any(c.islower() for c in password):
        score +=10
    if any(c.isupper() for c in password):
        score +=10
    if any(c.isdigit() for c in password):
        score +=10
    if any(c in string.punctuation for c in password):
        score +=10
    if entropy >50:
        score +=20

def main():
    print (f"Password Strength Checker :")
    password = input("enter a password to check :")

    result = score_password(password)
    print('\n.........Password Analysis ........')
    print(f"length      :{result['length']}")
    print(f"Entropy      :{result['entropy']}")
    print(f"Score      :{result['Score']}")
    print(f"verdict      :{result['verdict']}")

if __name__ == "__main__":
    main()