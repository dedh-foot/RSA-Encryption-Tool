# 🔐 RSA Encryption Tool (Beginner Project)

A simple Python-based **RSA encryption and decryption tool**, built from scratch to understand the fundamentals of asymmetric cryptography.  
This project generates RSA key pairs, saves them for each user, and allows encryption/decryption using those keys.  

---

## What This Project Does
- Generates **public and private RSA keys** for a given username  
- Saves keys inside a "keys/" folder  
- Encrypts and decrypts messages using the RSA algorithm  
- Demonstrates basic file handling and modular Python scripting  

---

## Folder Structure
RSA-Encryption-Tool/<br/>
│<br/>
├── keys/ → stores generated key files<br/>
│ ├── user_private.txt<br/>
│ ├── user_public.txt<br/>
│<br/>
├── rsa_encryption.py → main Python script<br/>
└── README.md → this file<br/>

---

## How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/<dedh-foot>/RSA-Encryption-Tool.git
   cd RSA-Encryption-Tool

2. Run the script
   ```bash
   python rsa_encryption.py

3. Follow on-screen prompts to:<br/>
Generate new keys<br/>
Encrypt messages<br/>
Decrypt messages<br/>

---

## Requirements

Python 3.x<br/>
No external libraries required (for now)

---

## Future Plans

This project is still a work in progress.

In upcoming updates, I plan to:<br/>
1. Store keys in PEM format<br/>
2. Add error handling and input validation<br/>
3. Possibly build a simple GUI for easier interaction<br/>

## About This Project

This project was created as part of my cybersecurity learning journey to better understand how encryption works under the hood.<br/>
I’ll continue improving and refactoring the code step by step.

Author: dedhfoot<br/>
Cybersecurity Student | Python Learner | Security Enthusiast<br/>
Feel free to fork, suggest improvements, or connect with me!<br/>


| ⚠️ Note: This project is for educational purposes only and not for production-level cryptography.
