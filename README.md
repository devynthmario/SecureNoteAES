# 🔐 SecureNoteAES - AES Encrypted Note-Taking App with Tkinter

**SecureNoteAES** is a desktop GUI application written in Python that allows users to securely write, encrypt, and store personal notes using **AES encryption** with a master key.

This project is based on [Atıl Samancıoğlu's SecretNotes project](https://github.com/atilsamancioglu/P11-SecretNotes) and has been extended with advanced encryption and usability features.

---

## ✨ Features

- ✅ Clean and responsive Tkinter GUI
- 🔐 AES-256 encryption using `cryptography` and `Fernet`
- 🧠 SHA-256 based key derivation from user password
- 📌 Save notes with custom titles
- 🔓 Decrypt saved encrypted notes using the master key
- 👁️ Show/hide password functionality
- 🚫 Input validation & exception handling
- 💾 Local file saving (as `.txt`)

---

## 📦 Technologies Used

- Python 3.x
- `tkinter` for graphical interface
- `cryptography` for AES-based encryption
- `hashlib` and `base64` for secure key generation

---

## 🚀 How to Use

1. **Install the required library**:
    ```bash
    pip install cryptography
    ```

2. **Run the app**:
    ```bash
    python main.py
    ```

3. **Steps**:
    - Enter a title for your note.
    - Type your secret message.
    - Set a master password (used for encryption).
    - Click **"Save & Encrypt"** to save the note securely.
    - To decrypt a note, paste the encrypted content into the message box, enter the password, and click **"Decrypt"**.

---

## 🔗 Credits & Acknowledgements

This project was **inspired by and built upon** the following open-source work:

> 🔗 [Atıl Samancıoğlu – P11-SecretNotes](https://github.com/atilsamancioglu/P11-SecretNotes)

Modifications & Improvements:
- Replaced custom cipher with **AES encryption** (Fernet)
- Added **SHA-256 key derivation**
- Improved UI with show/hide password
- Added robust error handling
- Reorganized UI layout for better UX

---

## 🧑‍💻 Author

Built and extended by Ahmet Şentürk
📬 https://github.com/devynthmario

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.  
Feel free to fork and build upon it — just give credit to the original and extended authors.

