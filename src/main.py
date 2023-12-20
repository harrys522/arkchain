import socket
import threading
import time

class Node:
    def __init__(self, user_id):
        self.user_id = user_id
        self.peers = []

def handle_client(client_socket, user):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"User {user.user_id} received message: {data}")
        except Exception as e:
            print(f"Error reading data from User {user.user_id}: {e}")
            break

    print(f"Connection with User {user.user_id} closed")
    client_socket.close()

def start_server(user):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', user.user_id + 8000))
    server_socket.listen(5)

    print(f"Server for User {user.user_id} listening on port {user.user_id + 8000}...")

    while True:
        try:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            client_handler = threading.Thread(target=handle_client, args=(client_socket, user))
            client_handler.start()
        except Exception as e:
            print(f"Error accepting connection for User {user.user_id}: {e}")

def send_message(peer, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', peer.user_id + 8000))
        client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message to User {peer.user_id}: {e}")
    finally:
        client_socket.close()

def main():
    # Create a UserGraph with nodes
    user1 = Node(1)
    user2 = Node(2)
    user3 = Node(3)

    user_graph = [user1, user2, user3]

    # Start a server for each user in a separate thread
    server_threads = []
    for user in user_graph:
        server_thread = threading.Thread(target=start_server, args=(user,))
        server_threads.append(server_thread)
        server_thread.start()

    # Allow some time for servers to start before sending messages
    time.sleep(2)

    # Simulate communication between nodes
    for user in user_graph:
        for peer in user.peers:
            if peer != user:
                message = f"Hello from User {user.user_id} to User {peer.user_id}"
                send_message(peer, message)

    # Wait for all server threads to complete
    for server_thread in server_threads:
        server_thread.join()

if __name__ == "__main__":
    main()