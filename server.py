import socket
import subprocess as sp

# ================= TO-DO ================= # 
# Allow 3 attempts before closing connection
# Blacklist IP addresses after too many failed attempts

def server():
    # Define server
    host = socket.gethostbyname(socket.gethostname()) 
    port = 1234

    # Create an INET streaming socket (i.e. IPv4 and TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    
        # Read whitelisted IPs and ports from file
    ip_file = open("allowed_ips.txt", "r")
    ip_list = [line.strip('\n') for line in ip_file]
    print(ip_list) 

    ip_file.close()
    
    port_file = open("allowed_ports.txt", "r")
    port_list = [int(line.strip('\n')) for line in port_file]
    print(port_list)

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
            print("Error: forbidden IP address")
        
        if address[1] not in port_list:
            conn.close()
            print("Error: forbidden port number")
    

        data = "Please enter the password below.\n"
        conn.send(data.encode())
        recv = str(conn.recv(1024).decode())
        print("Client > " + recv)
      
        if recv.lower().strip() != password:
            conn.send("Wrong password.".encode())
            conn.close()
            print("Error: wrong password! Connection closed.");
        
        elif recv.lower().strip() == password:
            sp.run(["./example_script.sh"])
            conn.send("Process completed.".encode())
            conn.close()
            print("Process completed. Connection closed.")
            
    conn.close()

    
if __name__ == "__main__":
    server()
