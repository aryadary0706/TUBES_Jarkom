import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Membuat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Menghubungkan ke server
        client_socket.connect((server_host, server_port))

        # Mengirim permintaan HTTP GET
        request_line = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
        client_socket.sendall(request_line.encode())

        # Menerima respons dari server
        response = client_socket.recv(4096)
        print("Response from server:")
        print(response.decode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
