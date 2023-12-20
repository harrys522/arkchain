import socket
import sys
ipv4 = socket.AF_INET
tcp = socket.SOCK_STREAM
host = ''
port = 43555

s = socket.socket(ipv4, tcp)
print("Socket successfully created")

# bind socket to a port
s.bind((host, port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(1)
print("socket is listening")
c = None
# a forever loop until we interrupt it or an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    break


def send(message):
    encoded = message.encode()
    c.send(encoded)


def receive():
    rMessage = c.recv(1024)
    return rMessage.decode()

while True:
    # Receive client messages
    rcvd = receive()
    if not rcvd:
        continue
    print("RECEIVED:", rcvd)

    # Authenticate new client (example function)
    if rcvd == 'AUTH':
        send('1')

    # Receive bloom filter encoded data
    if rcvd.__contains__('DATA'):
        mSplit = rcvd.split()
        size = mSplit[1]
        csvData = receive(size)
        # Put csvData into pandas somehow?


    # Close the connection with the client
    if rcvd == 'QUIT':
        c.close()
        # Breaking once connection closed
        break
