import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            
            # Send a response back to the client
            client_socket.send(f"Server received: {message}".encode('utf-8'))
        except:
            break

    # Close the connection when done
    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Main function to start the server
def start_server(host='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")
    
    while True:
        # Accept a new client connection
        client_socket, client_address = server.accept()
        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    start_server()
