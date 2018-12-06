# Remote Script Execution

## Introduction
Python script made to execute server code once client is authenticated. This will be used on a windows server to execute powershell code as a test.

To connect to the server (client.py is still work in progress), download the ncat tool, and use
```
$ ncat --source-port 4444 -nv <server_ip> 1234
```

The allowed ports, IP addresses and server ports can be changed.

## Additional Reading on Sockets:
* https://docs.python.org/2/library/socket.html
* https://docs.python.org/3.7/howto/sockets.html
