# 🔐 Python Secure Password Manager (CLI)

A simple, command-line interface (CLI) application developed to manage passwords locally. This tool allows users to store credentials securely in a text file, retrieve them instantly, and generate strong random passwords on the go using Python.

## ⚠️ Important Disclaimer
> **Educational Purpose Only:** This project saves passwords in a local text file (`passwordBook.txt`) without encryption. While it demonstrates core programming concepts, please **do not use this to store highly sensitive real-world data** (like banking passwords) without adding encryption layers.

## 🚀 Features

* **➕ Add Passwords:** Save website names and passwords to a file using a custom separator (`|`).
* **🎲 Generate Strong Passwords:** Built-in generator creates 12-character strong passwords using a mix of:
    * Uppercase & Lowercase letters (`string.ascii_letters`)
    * Numbers (`string.digits`)
    * Symbols (`string.punctuation`)
* **🔍 View Passwords:** Search for a password by entering the Site Name.
* **📂 Persistent Storage:** All data is saved in `passwordBook.txt`, ensuring data remains after the program closes.
* **🛡️ Error Handling:** Handles scenarios where the file doesn't exist yet.

## 🛠️ Concepts Applied

* **File Handling:** Uses append mode (`a`) to save data and read mode (`r`) to fetch data.
* **String Manipulation:** Uses `.split(" | ")` to separate the site name from the password when reading the file.
* **Random Module:** Uses `random.choices` for generating unpredictable passwords.
* **Global Variables:** Manages state within functions.

## 📂 Project Structure

```text
├── My-Password-Manager.py   # Main application script
├── passwordBook.txt.txt         # Database file (Auto-created)
└── README.md             # Project documentation

```
## 👨‍💻 Author

**Suresh Nuwan Tharaka**
*Aspiring Software Engineer & Undergraduate*

---
*Created as a part of my Python learning journey.*