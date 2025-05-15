import socket
import sys

def http_client(server_host, server_port, filename):
    # Membuat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menghubungkan ke server
    client_socket.connect((server_host, server_port))

    # Membuat permintaan HTTP GET
    request_line = f"GET /{filename} HTTP/1.1\r\n"
    headers = "Host: {}\r\n\r\n".format(server_host)
    request = request_line + headers

    # Mengirim permintaan ke server
    client_socket.sendall(request.encode())

    # Menerima respons dari server
    response = b""
    while True:
        part = client_socket.recv(4096)
        if not part:
            break
        response += part

    # Menutup koneksi
    client_socket.close()

    # Menampilkan respons
    print(response.decode())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    http_client(server_host, server_port, filename)
