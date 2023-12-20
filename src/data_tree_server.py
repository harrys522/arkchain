import socket
import threading
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from data_tree import DataTree

# Global AVL tree
data_tree = DataTree()

# Generate server's public-private key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

def handle_client(client_socket):
    try:
        # Send the server's public key to the client
        serialized_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        client_socket.send(serialized_public_key)

        # Receive the client's public key
        client_public_key_bytes = client_socket.recv(2048)
        client_public_key = serialization.load_pem_public_key(
            client_public_key_bytes,
            backend=default_backend()
        )

        # Create a node object for the client

        # Send the server's public key to the client
        serialized_server_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        client_socket.send(serialized_server_public_key)

        # Other logic

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9000))
    server_socket.listen(5)

    print("Server listening on port 9000...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()




if __name__ == "__main__":
    start_server()
