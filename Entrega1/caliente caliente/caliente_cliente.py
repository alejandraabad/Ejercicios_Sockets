import socket

IP = "10.0.2.15"
PORT = 8212

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    print("conexión establecida")
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))


#en el codigo del cliente :
#n_usuario = (input("Introduzca un numero "))

send_message = input("Introduzca un numero: ")
send_bytes = str.encode(send_message)
# We must write bytes, not a string
s.send(send_bytes)
print("mensaje enviado")


condition = True
while condition:
    respuesta = s.recv(2048).decode("utf-8")
    print (respuesta)
    if respuesta == 'FELICIDADES':
        condition = False
    else:
        mensaje = input('Vuelve a intentarlo: ')
        send_bytes = str.encode(mensaje)
        # We must write bytes, not a string
        s.send(send_bytes)

s.close()
