import socket

IP = "10.0.2.15"
PORT = 8002
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:

        mensaje = input("Tu (servidor) dices: ")
        salida = str.encode(mensaje)
        clientsocket.send(salida)
        if mensaje.lower() == "adios":
            condition=False
        else:
            entrada = clientsocket.recv(2048).decode("utf-8")
            print("El cliente te dice: ", entrada)
            if entrada.lower() == "adios":
                condition=False

    clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
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
