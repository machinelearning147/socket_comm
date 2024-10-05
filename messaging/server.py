import socket
import threading
import sys

# Function to handle receiving messages from the client
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    # Thread for receiving messages
    def receive_messages():
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                # Move the cursor up, print the message, and re-display the prompt
                sys.stdout.write(f"\r[{client_address}] {message}\nYou (Server): ")
                sys.stdout.flush()
            except:
                break

    # Thread for sending messages to the client
    def send_messages():
        while True:
            # Input message to send to the client
            message = input("You (Server): ")
            client_socket.send(message.encode('utf-8'))

    # Start both threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    # Close the connection when done
    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Main function to start the server
def start_server(host='127.0.0.1', port=5559):  # Adjust IP accordingly
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
