import hashlib

def crack_hash(target_hash, wordlist_path):
    with open(wordlist_path, 'r') as file:
        for line in file:
            word = line.strip()
            hashed = hashlib.md5(word.encode()).hexdigest()

            if hashed == target_hash:
                print(f"[+] Password found: {word}")
                return

    print("[-] Password not found")

if __name__ == "__main__":
    target = input("Enter hash: ")
    wordlist = "wordlists/common.txt"
    crack_hash(target, wordlist)
