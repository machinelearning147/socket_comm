import socket

# Function to send and receive messages from the server
def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    print(f"Connected to the server at {host}:{port}")
    
    while True:
        # Input message to send to the server
        message = input("You: ")
        if message.lower() == "exit":
            break
        client.send(message.encode('utf-8'))
        
        # Receive the server's response
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")
    
    client.close()

if __name__ == "__main__":
    start_client()