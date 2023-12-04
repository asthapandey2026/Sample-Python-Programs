import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))
    print("Connected to server.")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())                                                                  

        data = client_socket.recv(1024).decode()
        print("Received:", data)

    client_socket.close()

start_client()
