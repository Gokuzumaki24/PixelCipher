
# decryptor


from PIL import Image

def decrypt_message(image_path, passkey):
    img = Image.open(image_path)
    data = list(img.getdata())

    binary_data = ''
    for pixel in data:
        for value in pixel[:3]:  # R, G, B
            binary_data += str(value & 1)

    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        chars.append(chr(int(byte, 2)))
        if ''.join(chars).endswith("$$END$$"):
            break

    message = ''.join(chars).replace("$$END$$", "")

    # Validate passkey
    if ':' not in message:
        return "Invalid data or missing passkey."
    extracted_key, extracted_message = message.split(':', 1)
    if extracted_key != passkey:
        return "Wrong passkey!"
    return extracted_message
