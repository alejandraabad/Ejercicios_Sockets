import socket
import random

PORT = 8082
IP = "10.0.2.15"
MAX_OPEN_REQUESTS = 5

#na es el numero aleatorio que el servidor debe elegir al azar
na=(random.randrange(9))

#para calcular el resto de la division de la IP/10
numeros = IP.split(".")
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])
suma = a+b+c+d
division= int(suma / 10)
resto =(suma - division*10)

#si la IP coincide con el numero
def respuesta_correcta(clientsocket): 
    print(clientsocket)
    send_message =("TE HA TOCADO LA LOTERIA, EL NUMERO ERA: %i\n" %na)
    # Serializing the data to be transmitted
    send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)
    clientsocket.close() 

#si la IP no coincide con el numero
def respuesta_incorrecta(clientsocket): 
    print(clientsocket)
    send_message =("NO TE HA TOCADO LA LOTERIA, TU NUMERO ERA: %i \n" %resto)
    send_message +=("EL NUMERO PREMIADO ERA: %i\n" %na)
    send_message +=(hostname)
    # Serializing the data to be transmitted
    send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)
    clientsocket.close() 

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# bind the socket to a public host, and a well-known port
#hostname = socket.gethostname()
# Let's use better the local interface name
hostname=IP

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
        # in this case, we'll pretend this is a non threaded serv

        #dependiendo de si el resto coincide con na o no se ejecuta una función u otra:
        if resto == na:
            respuesta_correcta(clientsocket)
        else: 
            respuesta_incorrecta(clientsocket)

               
except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
