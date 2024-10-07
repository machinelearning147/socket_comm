import socket
import threading
import sys
import argparse

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
                print(f"\r[{client_address}] {message}\nYou (Server): ", end="")
                sys.stdout.flush()
            except:
                break

    # Thread for sending messages to the client
    def send_messages():
        while True:
            message = input("You (Server): ")
            if message.lower() == 'exit':
                client_socket.send("Server is disconnecting.".encode('utf-8'))
                break
            client_socket.send(message.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Main function to start the server
def start_server(host='127.0.0.1', port=5555, timeout=300):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    server.settimeout(timeout)  # Set timeout for inactivity
    print(f"[LISTENING] Server is listening on {host}:{port}")
    
    try:
        while True:
            try:
                client_socket, client_address = server.accept()
                thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            except socket.timeout:
                print(f"[TIMEOUT] Server has been inactive for {timeout} seconds. Shutting down...")
                break
    except KeyboardInterrupt:
        print("\n[SHUTTING DOWN] Server is shutting down manually...")
    finally:
        server.close()
        print("[SERVER CLOSED]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a TCP server.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP address of the server (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5555, help="Port number of the server (default: 5555)")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout for inactivity in seconds (default: 300)")
    args = parser.parse_args()

    start_server(host=args.host, port=args.port, timeout=args.timeout)
