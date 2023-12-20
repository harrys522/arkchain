import socket
import sys
ipv4 = socket.AF_INET
tcp = socket.SOCK_STREAM
host = '127.0.0.1'
port = 43555

s = socket.socket(ipv4, tcp)
print("Client socket successfully created")


def send(message):
    encoded = message.encode()
    s.send(encoded)


def receive():
    rMessage = s.recv(1024)
    return rMessage.decode()


# connecting to the server
s.connect((host, port))
print("the socket has successfully connected to server")
# receive data from the server and decoding to get the string.
print(receive())
# Ask server to authenticate and assign a client ID (Sample functionality)
send('AUTH')
clientID = receive()
print("Client ID is ", id)

# Load CSV

# BF_Encoding


# Send encoded records
records = 'Hello'
send('HELLO')
send('TESTs')

s.close()