import socket

def client():
    host = "127.0.0.1"
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("> ")
    exit_code = "close"

    while message.lower().strip() != exit_code:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print("Server > " + data)

        message = input("> ")
    client_socket.send(exit_code.encode())
    client_socket.close()

if __name__ == "__main__":
    client()
