import socket
import random
PORT = 8212
IP = "10.0.2.15"
MAX_OPEN_REQUESTS = 5
n_aleatorio =random.random()*99
n_aleatorio = int(n_aleatorio)
print (n_aleatorio)
def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:
        a = (clientsocket.recv(2048).decode("utf-8"))
        print(a)
        print("Read from the client", a)
        a = int(a)
        if a == n_aleatorio:
            mensaje='FELICIDADES'
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = False

        elif n_aleatorio - 10<=a <= n_aleatorio + 10:
            b = "Caliente Caliente"
            send_bytes = str.encode(b)
            clientsocket.send(send_bytes)
            condition = True

        elif a >n_aleatorio+10:
            c = "Frío Frío por arriba"
            send_bytes = str.encode(c)
            clientsocket.send(send_bytes)
            condition = True

        elif a <n_aleatorio-10:
            d = "Frío Frío por abajo"
            send_bytes = str.encode(d)
            clientsocket.send(send_bytes)
            condition = True

    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
