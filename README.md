# 🔐 SecureNoteAES - Encrypted Note-Taking App (Python + Tkinter)

**SecureNoteAES** is a desktop application built with Python and Tkinter that allows users to write, encrypt, save, and decrypt personal notes using strong AES encryption.

The main goal is to provide a simple, minimal, yet secure way to protect your thoughts or sensitive data on your local machine.

---

## 🎯 Features

- Clean and user-friendly graphical interface
- AES encryption with `cryptography` library (Fernet)
- SHA-256 password-to-key derivation
- Save notes with custom titles
- Decrypt encrypted messages with correct password
- Toggle password visibility
- Input validation and error handling

---

## 🧪 Technologies Used

- Python 3.x  
- `tkinter` for GUI  
- `cryptography` for AES encryption  
- `hashlib` and `base64` for key derivation  
- Standard exception handling

---

## 🚀 How to Use

1. **Install dependencies** (if not already):
    ```bash
    pip install cryptography
    ```

2. **Run the application**:
    ```bash
    python main.py
    ```

3. **Workflow**:
    - Enter a note title
    - Type your secret message
    - Set a master key (password)
    - Click **"Save & Encrypt"** to store it securely
    - To decrypt, paste the encrypted text into the message box and click **"Decrypt"** with the correct key

---

## 🔗 Reference & Inspiration

This project is inspired and partially based on the repository:  
🔗 [https://github.com/devynthmario/SecureNoteAES](https://github.com/devynthmario/SecureNoteAES)

Additional logic and UI improvements were made on top of the original idea.

---

## 🧑‍💻 Author

Made with ❤️ by [YourNameHere]  
Feel free to fork, modify, and improve!

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.  
If you use or adapt it, please give proper credit.

🔧 Sonraki adımlar:
YourNameHere yerine GitHub adını veya profil linkini koyabilirsin.

Gerekirse ekran görüntüsü (screenshot.png) ekleyip ![UI Screenshot](screenshot.png) gibi gösteririm.

Proje yapısını da eklemek istersen, 📁 Project Structure başlığı da oluşturabiliriz.

Hazırsan bu README'yi README.md olarak dosyaya kaydetmek için Python komutu da yazabilirim. Yardım edeyim mi?








Şunu dedin:
https://github.com/atilsamancioglu/P11-SecretNotes ben buradan yararlanıp geliştirim ona göre yaz


ChatGPT:
Harika! O zaman README'yi Atıl Samancıoğlu'nun P11-SecretNotes projesinden yararlandığını ve üzerine AES şifreleme, UI geliştirmeleri, hata yönetimi gibi eklemeler yaptığını belirtecek şekilde düzenliyorum.

İşte sana özel, profesyonel ve katkı belirten bir README.md dosyası 👇

markdown
Kopyala
Düzenle
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

## 🧑‍💻 Author

Built and extended by Ahmet Şentürk
📬 @devythmario

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.  
Feel free to fork and build upon it — just give credit to the original and extended authors.
