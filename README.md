# PixelCipher
Image-Based Cryptography Using Steganography in Python

📌 Project Description:

This project demonstrates a secure method of hiding encrypted messages inside images using the concept of steganography combined with cryptographic passkey protection. It provides a Graphical User Interface (GUI) through which users can encrypt and decrypt secret messages directly inside images, making data transmission more secure and less suspicious to attackers.

The hidden message is embedded at the pixel level (RGB values) of the image using Least Significant Bit (LSB) encoding, and is only accessible to users who know the correct passkey.


💡 Objectives:

To build a secure, user-friendly system to hide and retrieve secret text messages in images.

To use cryptographic validation to protect against unauthorized access.

To ensure image quality is preserved while hiding data.

To allow modular and maintainable Python code with separate encryption and decryption logic.



⚙️ Key Features:


🔐 Passkey-Protected Encryption – Only users with the correct passkey can decrypt the hidden message.

🖼️ Image Upload Functionality – Choose any standard image (JPG, PNG, BMP) for encryption or decryption.

👁️ Steganography Implementation – Uses LSB (Least Significant Bit) to hide message bits inside image pixels.

💬 Secure Message Extraction – Ensures that decryption fails if the passkey is wrong or the message is tampered.

💻 Tkinter GUI – A user-friendly interface with buttons to Encrypt, Decrypt, and Refresh.

📂 Custom Output Path – Encrypted images are saved to a specific path chosen by the developer.



🛠️ Tech Stack:


Language: Python 3

Libraries Used:

PIL (Pillow) – Image processing

Tkinter – GUI creation

os – File path and directory handling


🛡️ Security Measures:


Ensures data integrity by adding a special end delimiter $$END$$ to detect message corruption.

The passkey is embedded along with the message and is verified during decryption.

Any wrong key or tampered image will result in a failed decryption with appropriate user warning.


🔚 Conclusion:


This project provides a strong foundation for data hiding and basic encryption, showing how multimedia (images) can be used for secure communication.
