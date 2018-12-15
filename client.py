import socket
import getpass

def client():
    source_port = 4444
    # Gets IP address automatically
    source_host = socket.gethostbyname(socket.gethostname())
    print("Source host: {}".format(source_host))
    # Set server IP address manually
    host = "192.168.200.123"
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind((source_host, source_port))
    client_socket.connect((host, port))

    exit_codes = ["wrong password.", "process completed."]

    while True:

        data = client_socket.recv(1024).decode()
        print(data)
        if data.lower().strip() in exit_codes:
            break

        message = getpass.getpass("Password: ")
        client_socket.send(message.encode())
     

    client_socket.close()

if __name__ == "__main__":
    client()
