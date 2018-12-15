import socket
import subprocess as sp

# ================= TO-DO ================= # 
# Allow 3 attempts before closing connection
# Blacklist IP addresses after too many failed attempts

def server():
    # Define server
    try:
        host = socket.gethostbyname(socket.gethostname()) 
        port = 1234
    except Exception as e:
        print("ERROR: Can't create host, enter the host IP address manually.")
        raise e

    # Create an INET streaming socket (i.e. IPv4 and TCP)
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
    except Exception as e:
        print("ERROR: Can't create socket.")
        raise e 

    # Read whitelisted IPs and ports from file
    try:
        ip_file = open("allowed_ips.txt", "r")
        ip_list = [line.strip('\n') for line in ip_file]
        print("Allowed IP addresses: {}".format([ip for ip in ip_list])) 
    except IOError as e:
        print("ERROR: allowed_ips.txt can't be opened. Check if it is in the same directory and has the name 'allowed_ips.txt'.")
        raise e

    ip_file.close()
    
    try:
        port_file = open("allowed_ports.txt", "r")
        port_list = [int(line.strip('\n')) for line in port_file]
        print("Allowed port numbers: {}".format([port for port in port_list]))
    except IOError as e:
        print("ERROR: allowed_ports.txt can't be opened. Check if it is in the same directory and has the name 'allowed_ports.txt'.")
        raise e

    port_file.close()
    password = "testpassword"

    # Listen for 1 connection at a time
    server_socket.listen(1)
    print("{} listening on port {}".format(host, port))
    while True:
        conn, address = server_socket.accept()

        # Security checks, add allowed ip's and ports to lists
        print("Connection from {} on port {}".format(str(address[0]), str(address[1])))

        if str(address[0]) not in ip_list:
            conn.close()
            print("ERROR: forbidden IP address")
        
        if address[1] not in port_list:
            conn.close()
            print("ERROR: forbidden port number")
    

        data = "Please enter the password below.\n"
        conn.send(data.encode())
        recv = str(conn.recv(1024).decode())
        print("Client > " + recv)
      
        if recv.lower().strip() != password:
            conn.send("Wrong password.".encode())
            conn.close()
            print("Error: wrong password! Connection closed.");
        
        elif recv.lower().strip() == password:
            try:
                sp.run(["./example_script.sh"])
            except IOError as e:
                print("ERROR: Can't run executable. Please check if the path is correct.")
                raise e
            conn.send("Process completed.".encode())
            conn.close()
            print("Process completed. Connection closed.")
            
    conn.close()

    
if __name__ == "__main__":
    server()
