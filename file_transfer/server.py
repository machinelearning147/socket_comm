import socket

def receive_file(filename, host='0.0.0.0', port=5001):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection from a client
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Open the file to write the incoming data
    with open(filename, 'wb') as file:
        while True:
            # Receive data from the client
            data = connection.recv(1024)
            if not data:
                # Break the loop when no more data is sent
                break
            file.write(data)

    # Close the connection
    connection.close()
    print(f"File {filename} received successfully.")

if __name__ == "__main__":
    # File name where the received file will be saved
    filename = 'received_file.txt'
    receive_file(filename)
