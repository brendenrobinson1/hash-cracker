import hashlib


def load_rules(rules_path):
    rules = []

    with open(rules_path, "r") as file:
        for line in file:
            rule = line.strip()

            if rule:
                rules.append(rule)

    return rules


def apply_rule(word, rule):
    if rule == "original":
        return word

    elif rule == "capitalize":
        return word.capitalize()

    elif rule == "append_1":
        return word + "1"

    elif rule == "append_!":
        return word + "!"

    elif rule == "replace_a_@":
        return word.replace("a", "@")

    elif rule == "replace_o_0":
        return word.replace("o", "0")

    return word


def mutate(word, rules):
    variations = []

    variations.append(word)

    for rule in rules:
        mutated_word = apply_rule(word, rule)

        if mutated_word not in variations:
            variations.append(mutated_word)

    return variations


def crack_hash(target_hash, wordlist_path, rules_path):
    rules = load_rules(rules_path)

    with open(wordlist_path, "r") as file:
        for line in file:
            word = line.strip()

            for attempt in mutate(word, rules):
                hashed = hashlib.md5(attempt.encode()).hexdigest()

                if hashed == target_hash:
                    print(f"[+] Password found: {attempt}")
                    return

    print("[-] Password not found")


if __name__ == "__main__":
    target = input("Enter hash: ")

    wordlist = "wordlists/common.txt"
    rules = "rules/basic_rules.txt"

    crack_hash(target, wordlist, rules)
