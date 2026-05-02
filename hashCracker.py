import argparse
from hashcracker_core import crack_hash, SUPPORTED_ALGORITHMS


parser = argparse.ArgumentParser(description="Simple Password Cracker")

parser.add_argument("--hash", help="Hash to crack")
parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
parser.add_argument("--type", required=True, help="Hash type")
parser.add_argument("--hashfile", help="File containing hash")
parser.add_argument(
    "--rules",
    choices=["none", "light", "medium", "heavy"],
    default="light",
    help="Rule strength: none, light, medium, or heavy"
)

args = parser.parse_args()

if args.hashfile:
    with open(args.hashfile, "r") as f:
        target_hash = f.readline().strip()
elif args.hash:
    target_hash = args.hash
else:
    print("Error: You must provide --hash or --hashfile")
    exit()

algorithm = args.type.lower()

if algorithm not in SUPPORTED_ALGORITHMS:
    print("Error: Unsupported hash type")
    exit()

if len(target_hash) == 32:
    print("[INFO] Detected possible MD5 hash")
elif len(target_hash) == 40:
    print("[INFO] Detected possible SHA1 hash")
elif len(target_hash) == 64:
    print("[INFO] Detected possible SHA256 hash")

result = crack_hash(
    target_hash,
    algorithm,
    args.wordlist,
    rules=args.rules
)

if result:
    print("[FOUND] Password:", result)
else:
    print("[FAILED] Password not found.")