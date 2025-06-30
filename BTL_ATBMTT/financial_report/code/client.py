import socket
from utils import compress_file, encrypt_file, generate_key, save_key

HOST = 'HusbandMaterial'
PORT = 192.168.0.106

file_to_send = "financial_report.pdf"

# Nén
compressed_file = compress_file(file_to_send)

# Tạo và lưu key
key = generate_key()
save_key(key)

# Mã hóa file
encrypted_file = encrypt_file(compressed_file, key)

# Gửi file đã mã hóa
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open(encrypted_file, "rb") as file:
        data = file.read()
        s.sendall(data)
    print("Đã gửi file mã hóa thành công.")
