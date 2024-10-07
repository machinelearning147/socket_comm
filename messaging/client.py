import socket
import threading
import sys
import argparse

# Function to handle receiving messages from the server
def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    print(f"Connected to the server at {host}:{port}")

    # Thread for receiving messages
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"\rServer: {message}\nYou (Client): ", end="")
                sys.stdout.flush()
            except:
                break

    # Thread for sending messages to the server
    def send_messages():
        while True:
            message = input("You (Client): ")
            if message.lower() == 'exit':
                client.send("Client is disconnecting.".encode('utf-8'))
                break
            client.send(message.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()
    print("[DISCONNECTED] Client disconnected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a TCP client.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="IP address of the server (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5555, help="Port number of the server (default: 5555)")
    args = parser.parse_args()

    start_client(host=args.host, port=args.port)
