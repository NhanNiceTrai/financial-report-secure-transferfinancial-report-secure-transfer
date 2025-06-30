import socket
from utils import load_key, decrypt_file, decompress_file

HOST = 'localhost'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Đang chờ kết nối từ client...")
    conn, addr = s.accept()
    with conn:
        print(f"Kết nối từ {addr}")
        data = b''
        while True:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet

        # Lưu dữ liệu nhận được
        with open("received_encrypted.bin", "wb") as f:
            f.write(data)

        # Giải mã
        key = load_key()
        decrypted_zip = decrypt_file("received_encrypted.bin", key)

        # Giải nén
        decompress_file(decrypted_zip)
        print("Đã nhận và giải mã + giải nén thành công.")
