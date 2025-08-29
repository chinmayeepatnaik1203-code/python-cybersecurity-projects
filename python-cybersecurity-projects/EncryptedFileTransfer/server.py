import socket
from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

host = "0.0.0.0"
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"[*] Server listening on {host}:{port}")

conn, addr = server.accept()
print(f"[+] Connected by {addr}")

# Receive the filename
filename = conn.recv(1024).decode()
conn.send(b"ACK")  # send ack back

# Receive encrypted file data
encrypted_data = conn.recv(10000000)  # 10MB max
decrypted_data = cipher.decrypt(encrypted_data)

# Save decrypted file
with open("received_" + filename, "wb") as f:
    f.write(decrypted_data)

print(f"[+] File received and saved as received_{filename}")

conn.close()
server.close()