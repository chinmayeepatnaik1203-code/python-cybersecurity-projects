# 🛡 Python Cybersecurity Projects  

Welcome to my *Cybersecurity Projects Repository* 🎓  
This repository contains multiple Python-based projects showcasing my skills in *cryptography, networking, and security tools*.  
All projects are beginner-friendly, well-documented, and focused on *hands-on cybersecurity learning*.  

---

## 📂 Projects Included

### 1️⃣ 🔐 Encrypted File Transfer
- *Goal*: Securely transfer files between client and server using AES encryption (Fernet).
- *Features*:
  - Client-Server communication using sockets  
  - AES symmetric encryption  
  - Encrypted file storage & transfer  
- *Run Instructions*:
  ```bash
  # Start the server
  python EncryptedFileTransfer/server.py

  # Run the client
  python EncryptedFileTransfer/client.py
  ---

### 2️⃣ 🔎 TLS Analyzer Tool
- *Goal*: Analyze SSL/TLS connections and extract security details from network traffic.  
- *Features*:
  - Parse TLS Handshake packets with *Wireshark & Scapy*  
  - Extract extensions: SNI, ALPN, OCSP Stapling  
  - Check for weak ciphers & deprecated protocols  
  - Generate report of server configuration security  

🛠 *How to run*:
```bash
python tls_analyzer.py --pcap traffic.pcap
---
