import socket
import subprocess as sp

def server():
    # Define server
    host = "localhost" 
    port = 1234

    # Create an INET streaming socket (i.e. IPv4 and TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    
    # Listen for 1 connection at a time
    server_socket.listen(1)
    print("{} listening on port {}".format(host, port))
    conn, address = server_socket.accept()
    
    # Read whitelisted IPs and ports from file
    ip_file = open("allowed_ips.txt", "r")
    ip_list = [line[:-1] for line in ip_file]
    print(ip_list) 

    ip_file.close()
    
    port_file = open("allowed_ports.txt", "r")
    port_list = [int(line[:-1]) for line in port_file]
    print(port_list)

    port_file.close()

    # Security checks, add allowed ip's and ports to lists
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
        data = "Please enter the password below.\n"
        conn.send(data.encode())
        recv = str(conn.recv(1024).decode())
        print("Client > " + recv)
        
        if recv.lower().strip() != password:
            conn.send("Wrong password.".encode())
            conn.close()
            return "ERROR: Wrong password"
        
        elif recv.lower().strip() == password:
            #output = str(sp.run(["ls"], capture_output=True).stdout) + "\n"
            #print(sp.run(["ls"], capture_output=True).stdout)
            #conn.send(output.encode())
<<<<<<< HEAD
            sp.run(["/home/arched/Projects/RemoteExec/python/example_script.sh"])
            conn.send("Process completed.".encode())
=======
            sub.run(["/path/to/example_script.sh"])
>>>>>>> d4bbdc181da2f2aa19056dba42d5748d589df08d
            server_socket.close()
            conn.close()
            return "Process Complete"
            

    conn.close()

    
if __name__ == "__main__":
    print(server())
