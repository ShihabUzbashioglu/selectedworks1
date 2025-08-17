import socket

import sys 

args = sys.argv
sock = socket.socket( socket.AF_INET,socket.SOCK_STREAM)

print(f"start scanning on {args[1]}")

open_ports = []

for port in range(int(args[2]),int(args[3])):
    try:
    # google.com 80

    #if running port is closed
    #if exited port is opened
    sock.settimeout(1)
    sock.connect(args[1],port)
    open_ports.append(port)
    print(f'{port} [opened] {Socket.getservebyport({port})}')
    #sock.connect("google.com",4444)
    except:
        print(f'{port} closed')



print("----------------------------------------------")

for x in open_ports:
    print(f"{x} [OPEN]")