import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)
    print("Server started. Waiting for connections...")

    client_socket, client_address = server_socket.accept()
    print("Connected to", client_address)

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received:", data)

        message = input("Enter your message: ")
        client_socket.send(message.encode())

    client_socket.close()
    # server_socket.close()

start_server()
