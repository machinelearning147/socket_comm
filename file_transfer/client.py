import socket

def send_file(filename, server_ip='127.0.0.1', server_port=5001):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    # Open the file to read the data
    with open(filename, 'rb') as file:
        # Read and send the file data in chunks
        chunk = file.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = file.read(1024)

    # Close the connection
    client_socket.close()
    print(f"File {filename} sent successfully.")

if __name__ == "__main__":
    # The name of the file you want to send
    filename = 'file_to_send.txt'
    # Change server_ip to the IP address of the receiving machine
    server_ip = '192.168.31.184'  # Example server IP
    send_file(filename, server_ip)
