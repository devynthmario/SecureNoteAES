from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib


def generate_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_message(password: str, message: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()


def decrypt_message(password: str, encrypted_message: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message.encode())
    return decrypted.decode()


def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0", END).strip()
    master_secret = master_secret_input.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please enter all info")
    else:
        try:
            message_encrypted = encrypt_message(master_secret, message)
            with open("mysecret.txt", "a") as file:
                file.write(f"\n{title}\n{message_encrypted}")
            messagebox.showinfo(title="Success", message="Note saved and encrypted successfully.")
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))
        finally:
            title_entry.delete(0, END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0", END)


def deycrypt_notes():
    message_encrypted = input_text.get("1.0", END).strip()
    master_secret = master_secret_input.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info")
    else:
        try:
            decrypted_message = decrypt_message(master_secret, message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Invalid key or message.\n\nDetails: {e}")


window = Tk()
window.title("Secret Notes (AES Encrypted)")
window.config(padx=30, pady=30)


try:
    photo = PhotoImage(file="topsecret.png")
    canvas = Canvas(window, width=268, height=188)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.pack()
except:
    pass  # If image not found, just skip


FONT = ("Verdana", 14, "normal")


title_info_label = Label(window, text="Enter your title", font=FONT)
title_info_label.pack()
title_entry = Entry(window, width=30)
title_entry.pack()


input_info_label = Label(window, text="Enter your secret", font=FONT)
input_info_label.pack()
input_text = Text(window, width=50, height=10)
input_text.pack()

master_secret_label = Label(window, text="Enter master key", font=FONT)
master_secret_label.pack()
master_secret_input = Entry(window, width=30, show="*")
master_secret_input.pack()


def toggle_password():
    if show_password.get():
        master_secret_input.config(show="")
    else:
        master_secret_input.config(show="*")

show_password = BooleanVar()
Checkbutton(window, text="Show password", variable=show_password, command=toggle_password).pack()


save_button = Button(window, text="Save & Encrypt", command=save_and_encrypt_notes, bg="green", fg="white", font=FONT)
save_button.pack(pady=5)

decrypt_button = Button(window, text="Decrypt", command=deycrypt_notes, bg="blue", fg="white", font=FONT)
decrypt_button.pack(pady=5)

window.mainloop()
