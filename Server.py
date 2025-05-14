import socket
import threading
import os

# Fungsi untuk menangani permintaan klien
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Received request:\n{request}")

    # Parsing request untuk mendapatkan nama file
    lines = request.splitlines()
    if len(lines) > 0:
        # Mengambil nama file dari request
        request_line = lines[0]
        filename = request_line.split()[1][1:]  # Menghapus '/' di depan nama file

        # Menyiapkan respons
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                response_body = f.read()
            response_header = 'HTTP/1.1 200 OK\r\n'
        else:
            response_body = b"<h1>404 Not Found</h1>"
            response_header = 'HTTP/1.1 404 Not Found\r\n'

        # Mengirim header dan body respons
        response = response_header + 'Content-Length: {}\r\n\r\n'.format(len(response_body))
        client_socket.sendall(response.encode() + response_body)
    
    client_socket.close()

# Fungsi utama untuk menjalankan server
def run_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    run_server()
