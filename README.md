# 🔐 Python Secure Password Manager (CLI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/nuwa22/python-cli-password-manager)

**A simple yet powerful Command Line Interface (CLI) tool to securely manage your passwords locally.**

---

## ⚠️ Important Disclaimer

> **This project is for Educational Purposes Only.**  
> Passwords are currently stored in plain text (`passwordBook.txt`).  
> **Do not use this for real sensitive data** (banking, email, etc.) without adding proper encryption (like `cryptography` library).

---

## ✨ Features

- ➕ **Add Passwords** – Save website name & password
- 🎲 **Strong Password Generator** – 12-character random passwords
- 🔍 **Search Passwords** – Instantly find saved credentials
- 📂 **Persistent Storage** – Data remains even after closing the program
- 🛡️ **Error Handling** – Works even if the file doesn't exist

---

## 🛠️ Technologies & Concepts Used

- **Python** – Core Language
- **File Handling** – Read & Append modes
- **Random Module** – `random.choices()` for password generation
- **String Manipulation** – Splitting with custom separator
- **Error Handling** – Try-Except blocks

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/nuwa22/python-cli-password-manager.git

# 2. Go to the project folder
cd python-cli-password-manager

# 3. Run the application
python My-Password-Manager.py
```
├── My-Password-Manager.py          # Main application
├── passwordBook.txt                # Auto-created database file
├── README.md                       # Documentation
└── requirements.txt                # (Future - dependencies)

👨‍💻 Author
Suresh Nuwan Tharaka
Aspiring Data Scientist & Cybersecurity Enthusiast
Undergraduate | Python | PyTorch | Scapy

