import socket

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP/IP socket
    server_address = ('localhost', 8080)
    sock.connect(server_address)
    
    try:
        message = 'GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n' # request to the server
        sock.sendall(message.encode())
        data = sock.recv(1024) # receive the response from the server
        print(f'Response from server:\n{data.decode()}')
    finally:
        sock.close() # closing the socket

if __name__ == '__main__':
    run_client()