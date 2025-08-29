import ssl, socket

def get_cert_info(hostname, port=443):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.connect((hostname, port))
        cert = s.getpeercert()
        return cert

if _name_ == "_main_":
    site = "google.com"
    cert = get_cert_info(site)
    print(f"Certificate for {site}:")
    print(cert)