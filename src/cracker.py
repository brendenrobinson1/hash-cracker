import hashlib

def mutate(word):
    variations = []

    variations.append(word)
    variations.append(word.capitalize())
    variations.append(word + "1")
    variations.append(word + "!")
    variations.append(word.replace("a", "@"))
    variations.append(word.replace("o", "0"))

    return variations

def crack_hash(target_hash, wordlist_path):
    with open(wordlist_path, 'r') as file:
        for line in file:
            word = line.strip()

            for attempt in mutate(word):
                hashed = hashlib.md5(attempt.encode()).hexdigest()

                if hashed == target_hash:
                    print(f"[+] Password found: {attempt}")
                    return

    print("[-] Password not found")

if __name__ == "__main__":
    target = input("Enter hash: ")
    wordlist = "wordlists/common.txt"
    crack_hash(target, wordlist)
