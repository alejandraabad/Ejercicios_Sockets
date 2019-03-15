import socket

IP = "10.0.2.15"
PORT = 8002

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))

except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

condition = True

while condition:
    mensaje_entrada = s.recv(2048).decode("utf-8")
    print("El servidor te dice: ", mensaje_entrada)
    if mensaje_entrada.lower() == "adios":
        condition = False
    else:
        mensaje_salida = input("Tu (cliente) respondes: ")
        salida = str.encode(mensaje_salida)
        s.send(salida)
        if mensaje_salida.lower() == "adios":
            condition = False

s.close()
