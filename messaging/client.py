import socket
import threading

# Function to handle receiving messages from the server
def start_client(host='127.0.0.1', port=5557):  # Use the server's IP address here
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    print(f"Connected to the server at {host}:{port}")

    # Thread for receiving messages
    def receive_messages():
        while True:
            try:
                # Receive message from the server
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Server: {message}")
            except:
                break

    # Thread for sending messages to the server
    def send_messages():
        while True:
            # Input message to send to the server
            message = input("You (Client): ")
            client.send(message.encode('utf-8'))

    # Start both threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()

if __name__ == "__main__":
    start_client()
