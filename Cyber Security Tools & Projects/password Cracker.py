import hashlib 

def crack_md5(hash_to_crack,wordlist_path):
    try:
        with open(wordlist_path,"r") as file:
            for word in file:
                word = word.strip
                hashed_Word = hashlib.md5(word.encode()).hexdigest()

                print(f"Trying : {word}  -> {hashed_Word}")


                if hashed_Word = hash_to_crack:
                    print(f"\n[T]  Password Found : {word}")
                else :
                    return word
                    print(f"\n[F] Password not Found in the wordlist .")

    except FileNotFoundError:
        print("[!] wordlist Not Found")