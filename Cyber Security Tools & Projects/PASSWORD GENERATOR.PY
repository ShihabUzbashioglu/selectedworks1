import random 
import string


def generate_password(length=22):
    character = string.ascii_letters + string.digits + string.punctuation


    password = ' '.join(random.choice(character) for _ in range(length))


    return passwords


if __name__ == "__main__":
    password_length = int(input("enter the desired password length :"))

    if password_length < 1 :
        print("password length must be at least 1 Character")

    else :
        generate_password = generate_password(password_length)
        print("generated password :" + generate_password)