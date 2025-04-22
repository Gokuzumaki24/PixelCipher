
#encryptor

 
from PIL import Image
import os

def encrypt_message(message, passkey, image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Embed the passkey and message, with a strong end delimiter
    full_message = f"{passkey}:{message}$$END$$"
    binary_message = ''.join(format(ord(char), '08b') for char in full_message)

    data = list(img.getdata())
    new_data = []
    msg_index = 0

    for pixel in data:
        r, g, b = pixel
        if msg_index < len(binary_message):
            r = (r & ~1) | int(binary_message[msg_index])
            msg_index += 1
        if msg_index < len(binary_message):
            g = (g & ~1) | int(binary_message[msg_index])
            msg_index += 1
        if msg_index < len(binary_message):
            b = (b & ~1) | int(binary_message[msg_index])
            msg_index += 1
        new_data.append((r, g, b))

    img.putdata(new_data)
    encrypted_dir = r"C:\Users\Rishabh\OneDrive\Desktop\PixelCipher\img"
    os.makedirs(encrypted_dir, exist_ok=True)
    encrypted_image_path = os.path.join(encrypted_dir, f"encrypted_{os.path.basename(image_path)}")

    img.save(encrypted_image_path)
    return encrypted_image_path
