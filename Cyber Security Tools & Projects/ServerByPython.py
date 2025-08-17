import socket


server_ip = "192.168.1.1"
Server_port = 4444


socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.bind(server_ip,Server_port)
socket_server.listen(3)

print(f'listenning on {server_ip}:{Server_port}')

while True :
    client_socket.client_address = socket_server.accept()
    print(f'connection from {client_socket}')


    while True :

        message = client_socket.recv(1024)
        if not message :
            break
        print(f'client : {message.decode('UTF-8')}')
        message_input = input("message :")
        client_socket.sendall(message_input.encode('UTF-8'))

socket_server.close