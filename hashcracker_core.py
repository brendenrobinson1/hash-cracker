import hashlib
import time
from rules import mutate_word


SUPPORTED_ALGORITHMS = {
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512"
}


def hash_password(password, algorithm):
    password_bytes = password.encode("utf-8")

    if algorithm == "md5":
        return hashlib.md5(password_bytes).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password_bytes).hexdigest()
    elif algorithm == "sha224":
        return hashlib.sha224(password_bytes).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password_bytes).hexdigest()
    elif algorithm == "sha384":
        return hashlib.sha384(password_bytes).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(password_bytes).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm.")


def crack_hash(target_hash, algorithm, wordlist_path, rules="light", status=None):
    start_time = time.time()
    attempts = 0

    target_hash = target_hash.strip().lower()
    algorithm = algorithm.strip().lower()
    rules = rules.strip().lower()

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError("Unsupported hash algorithm.")

    if status is not None:
        status["running"] = True
        status["progress"] = 0
        status["attempts"] = 0
        status["total"] = 0
        status["found"] = False
        status["password"] = None
        status["time"] = 0
        status["speed"] = 0

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        for word in file:
            mutations = mutate_word(word, rules)

            for i, password in enumerate(mutations):
                if i > 10000:  # limit attempts per word
                    break
                attempts += 1

                hashed_attempt = hash_password(password, algorithm)

                elapsed = time.time() - start_time
                speed = attempts / elapsed if elapsed > 0 else 0

                if status is not None:
                    status["attempts"] = attempts
                    status["progress"] = int((attempts / 100000) * 100)
                    if status["progress"] > 100:
                        status["progress"] = 100
                    status["time"] = round(elapsed, 2)
                    status["speed"] = round(speed, 2)

                if hashed_attempt == target_hash:
                    if status is not None:
                        status["running"] = False
                        status["found"] = True
                        status["password"] = password
                        status["progress"] = 100

                    return password

    if status is not None:
        status["running"] = False
        status["found"] = False
        status["password"] = None
        status["progress"] = 100

    return None
