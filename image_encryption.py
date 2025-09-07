from PIL import Image
import numpy as np
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    encrypted = arr ^ key
    Image.fromarray(encrypted.astype(np.uint8)).save(output_path)
    print(f"Encrypted image saved to {output_path}")
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    decrypted = arr ^ key
    Image.fromarray(decrypted.astype(np.uint8)).save(output_path)
    print(f"Decrypted image saved to {output_path}")
key = 123
encrypt_image("C:/vscode/python/input.jpg ", "C:/vscode/python/encrypted.jpg", key)
decrypt_image("C:/vscode/python/encrypted.jpg", "C:/vscode/python/restored.jpg", key)