# 🔐 Hash Cracker Tool

## 📌 Overview

This project is a custom-built password cracking tool designed to simulate real-world password auditing techniques. It demonstrates how weak passwords can be compromised using dictionary attacks and rule-based mutations.

> ⚠️ This tool is intended for **educational and ethical use only**.

---

## 🚀 Features

* Dictionary-based password cracking
* Custom wordlist support
* Rule-based mutations (e.g., replacing letters with symbols, adding numbers)
* Brute-force fallback (optional)
* Performance optimization (planned: multithreading)

---

## 🧠 How It Works

1. A target hash is provided by the user
2. The tool iterates through a wordlist
3. Each word is optionally modified using mutation rules
4. The hash of each attempt is compared to the target
5. If a match is found → password is cracked

---

## 🛠️ Technologies Used

* Python / PHP (update based on your implementation)
* Hashing algorithms (MD5, SHA-1, SHA-256, etc.)
* Command-line interface (CLI)

---

## 📂 Project Structure

/hash-cracker
│── wordlists/
│── rules/
│── src/
│── README.md

---

## ▶️ Usage

```bash
python cracker.py --hash <HASH> --wordlist wordlists/common.txt
```

---

## 🧪 Example

**Input Hash:**
5f4dcc3b5aa765d61d8327deb882cf99

**Cracked Password:**
password

---

## 🔐 Ethical Use

This project is strictly for:

* Learning cybersecurity concepts
* Practicing password security auditing
* Demonstrating vulnerabilities in weak password systems

Do NOT use this tool on systems you do not own or have permission to test.

---

## 📈 Future Improvements

* Multithreading for faster cracking
* GPU acceleration (long-term)
* Web interface (Flask)
* Advanced rule engine (custom mutation sets)

---

## 👤 Author

Brenden Robinson

---

## ⭐ Notes

This project is part of a broader cybersecurity portfolio, including:

* Vulnerable vs Secure Web Application (Harry’s Hot Sauce)
* Security audit reports
* Penetration testing practice
