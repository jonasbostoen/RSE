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

In this example I've called a shell script with the subprocess library, but you can change it to execute other things as well. Read the [subprocess documentation](https://docs.python.org/3.7/library/subprocess.html) for more information.

## Additional Reading on Sockets:
* https://docs.python.org/3.7/library/socket.html
* https://docs.python.org/3.7/howto/sockets.html
