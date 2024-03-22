import socket

def create_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP/IP socket
    server_address = ('localhost', 8080)
    sock.bind(server_address)
    sock.listen(1)
    print(f'Server running on port {server_address[1]}...')
    
    while True:
        connection, client_address = sock.accept() # waiting for a connection
        try:
            print(f'Connection from {client_address}')
            request = connection.recv(1024) # receiving the request from the client
            response = b'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n<html><head><style>body {background-color:black;}</style></head><body><h1 style="color:yellow;">COMPUTER NETWORK PROJECT</h1><h2 style="color:red;">WEB SERVER</h2><img src="https://images.pexels.com/photos/691668/pexels-photo-691668.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt=""height="500",width="500"></body></html>'
            connection.sendall(response) # sending a response back to the client
        finally:
            connection.close() # close the connection

if __name__ == '__main__':
    create_server()