import zipfile
from cryptography.fernet import Fernet

# Tạo key mã hóa AES
def generate_key():
    return Fernet.generate_key()

# Lưu key vào file
def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Đọc key từ file
def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Nén file .pdf/.csv/.xlsx...
def compress_file(input_file, output_file="compressed.zip"):
    with zipfile.ZipFile(output_file, 'w') as zipf:
        zipf.write(input_file)
    return output_file

# Giải nén
def decompress_file(zip_file, output_dir="./"):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_dir)

# Mã hóa file nén
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = fernet.encrypt(file.read())
    with open("encrypted_data.bin", "wb") as enc_file:
        enc_file.write(encrypted_data)
    return "encrypted_data.bin"

# Giải mã
def decrypt_file(encrypted_file, key):
    fernet = Fernet(key)
    with open(encrypted_file, "rb") as file:
        decrypted_data = fernet.decrypt(file.read())
    with open("decrypted_data.zip", "wb") as dec_file:
        dec_file.write(decrypted_data)
    return "decrypted_data.zip"
