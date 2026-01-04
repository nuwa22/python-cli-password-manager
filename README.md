# 🔐 Python Secure Password Manager (CLI)

A simple yet functional Command-Line Interface (CLI) application developed to manage passwords locally. This tool allows users to store credentials securely in a text file, retrieve them instantly, and generate strong random passwords on the go.

## ⚠️ Important Disclaimer
> **Educational Purpose Only:** This project saves passwords in a local text file without advanced encryption. While it demonstrates core programming concepts, please **do not use this to store highly sensitive real-world data** (like banking passwords) without adding encryption layers.

## 🚀 Features

* **➕ Add Passwords:** Save website names and passwords securely to a file.
* **🔍 View Passwords:** Instantly search for a password using the website name (utilizes Python's efficient Dictionary `.get()` method).
* **🎲 Generate Passwords:** Built-in strong password generator using Python's `random` module (Mix of letters, numbers, and symbols).
* **📂 Persistent Storage:** All data is saved in `passwords.txt`, so nothing is lost when you close the program.

## 🛠️ Concepts Applied

* **Dictionaries:** Used for fast data lookup and storage structure.
* **File Handling:** Reading from and writing to text files (`a+` and `r` modes).
* **Random Module:** Generating unpredictable strings for security.
* **String Operations:** formatting and parsing text data.

## 📂 Project Structure

```text
├── password_manager.py   # Main application script
├── passwordBook.txt.txt         # Database file (Auto-created)
└── README.md             # Project documentation

```
## 👨‍💻 Author

**Suresh Nuwan Tharaka**
*Aspiring Software Engineer & Undergraduate*

---
*Created as a part of my Python learning journey.*