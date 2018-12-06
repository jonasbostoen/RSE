import socket
import subprocess as sub

def server():
    # Define server
    host = "localhost" 
    port = 1234

    # Create an INET streaming socket (i.e. IPv4 and TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("{} listening on port {}".format(host, port))
    conn, address = server_socket.accept()

    # Security checks, add allowed ip's and ports to lists
    ip_list = ["127.0.0.1"]
    port_list = [1234, 4444]
    print("Connection from {} on port {}".format(str(address[0]), str(address[1])))

    if str(address[0]) not in ip_list:
        conn.close()
        return "ERROR: Forbidden IP address"
        
    if address[1] not in port_list:
        conn.close()
        return "ERROR: Forbidden port number"
    
    recv = 1 
    password = "testpassword"

    while recv:
        data = "password > "
        conn.send(data.encode())
        recv = str(conn.recv(1024).decode())
        print("Client > " + recv)
        
        if recv.lower().strip() != password:
            conn.close()
            return "ERROR: Wrong password"
        
        elif recv.lower().strip() == password:
            #output = str(sub.run(["ls"], capture_output=True).stdout) + "\n"
            #print(sub.run(["ls"], capture_output=True).stdout)
            #conn.send(output.encode())
            sub.run(["/path/to/example_script.sh"])
            server_socket.close()
            conn.close()
            return "Process Complete"
            

    conn.close()

    
if __name__ == "__main__":
    print(server())
