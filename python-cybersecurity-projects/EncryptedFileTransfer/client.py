import socket
from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Connect to server
host = "127.0.0.1"  # Server IP
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Pick a file to send
filename = "hello.txt"   # you can change this to any file on your system
with open(filename, "rb") as f:
    data = f.read()

# Encrypt the file
encrypted_data = cipher.encrypt(data)

# Send the filename first
client.send(filename.encode())
ack = client.recv(1024)  # wait for server ack

# Send the encrypted file
client.sendall(encrypted_data)

print(f"[+] Encrypted file '{filename}' sent successfully!")

client.close()