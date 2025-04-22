#gui part 

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from encryptor import encrypt_message
from decryptor import decrypt_message
import os

# Ensure the img folder exists
if not os.path.exists("img"):
    os.makedirs("img")

# Main window setup
root = tk.Tk()
root.title("Image Cryptography")
root.geometry("500x400")

# Refresh function
def refresh_app():
    root.destroy()
    main()

# Encrypt window setup
def open_encrypt_window():
    encrypt_window = tk.Toplevel(root)
    encrypt_window.title("Encrypt Message")
    encrypt_window.geometry("600x500")

    # Image upload
    lbl_image = tk.Label(encrypt_window)
    lbl_image.pack(pady=10)

    image_path = ""

    def upload_image():
        nonlocal image_path
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            image_path = file_path
            img = Image.open(file_path)
            img = img.resize((300, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            lbl_image.configure(image=img)
            lbl_image.image = img
            messagebox.showinfo("Success", "Image loaded successfully!")

    # Input fields
    tk.Button(encrypt_window, text="Upload Image", command=upload_image).pack(pady=5)
    tk.Label(encrypt_window, text="Enter Message:").pack(pady=5)
    message_entry = tk.Entry(encrypt_window, width=60)
    message_entry.pack(pady=5)
    tk.Label(encrypt_window, text="Enter Passkey:").pack(pady=5)
    passkey_entry = tk.Entry(encrypt_window, width=60, show="*")
    passkey_entry.pack(pady=5)

    def encrypt_action():
        message = message_entry.get()
        passkey = passkey_entry.get()
        try:
            encrypted_image_path = encrypt_message(message, passkey, image_path)
            encrypted_image_path = os.path.join('img', encrypted_image_path)
            if encrypted_image_path:
                messagebox.showinfo("Success", f"Message encrypted successfully!\nSaved at: {os.path.abspath(encrypted_image_path)}")
            else:
                messagebox.showerror("Error", "Encryption failed!")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")

    tk.Button(encrypt_window, text="Encrypt", command=encrypt_action).pack(pady=10)

# Decrypt window setup
def open_decrypt_window():
    decrypt_window = tk.Toplevel(root)
    decrypt_window.title("Decrypt Message")
    decrypt_window.geometry("600x500")

    # Image upload
    lbl_image = tk.Label(decrypt_window)
    lbl_image.pack(pady=10)

    image_path = ""

    def upload_image():
        nonlocal image_path
        file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            image_path = file_path
            img = Image.open(file_path)
            img = img.resize((300, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            lbl_image.configure(image=img)
            lbl_image.image = img  # Keep a reference to avoid garbage collection
            messagebox.showinfo("Success", "Encrypted image loaded successfully!")

    # Input fields
    tk.Button(decrypt_window, text="Upload Image", command=upload_image).pack(pady=5)
    tk.Label(decrypt_window, text="Enter Passkey:").pack(pady=5)
    passkey_entry = tk.Entry(decrypt_window, width=60, show="*")
    passkey_entry.pack(pady=5)
    decrypted_message = tk.Text(decrypt_window, height=5, width=60)
    decrypted_message.pack(pady=5)

    def decrypt_action():
        passkey = passkey_entry.get()
        try:
            decrypted = decrypt_message(image_path, passkey)
            if decrypted:
                decrypted_message.delete(1.0, tk.END)
                decrypted_message.insert(tk.END, decrypted)
                messagebox.showinfo("Success", "Message decrypted successfully!")
            else:
                messagebox.showerror("Error", "Decryption failed!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

    tk.Button(decrypt_window, text="Decrypt", command=decrypt_action).pack(pady=10)


# Main window buttons
btn_encrypt = tk.Button(root, text="Encryptor", command=open_encrypt_window, width=20)
btn_encrypt.pack(pady=20)

btn_decrypt = tk.Button(root, text="Decryptor", command=open_decrypt_window, width=20)
btn_decrypt.pack(pady=20)

btn_refresh = tk.Button(root, text="Refresh", command=refresh_app, width=20)
btn_refresh.pack(pady=20)

# Run the GUI loop
def main():
    root.mainloop()

main()


