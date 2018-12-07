# Remote Script Execution

## Introduction
Python script made to execute server code once client is authenticated. This will be used on a windows server to execute powershell code as a test.

To connect to the server, use netcat or ncat (ncat is a newer netcat, comes with nmap):
```
$ nc --local-port 4444 -nv <server_ip> 1234
```
```
$ ncat --source-port 4444 -nv <server_ip> 1234
```
The allowed ports, IP addresses and server ports can be changed.

Or you can use the Python client.py script, which is safer because it obscures password prompts.

## Additional Reading on Sockets:
* https://docs.python.org/2/library/socket.html
* https://docs.python.org/3.7/howto/sockets.html
