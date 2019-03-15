import socket
import sys
IP = "10.0.2.15"
PORT = 8086

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((IP, PORT))

def menu():
    print("Las operaciones de nuestra calculadora son:")
    print("0. Salir")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

try:
    menu()
    operacion = str(input("Escriba el número de la operación "))
    operacion = int(operacion)
    if operacion != 0:
        numero_1 = str(input("Introduzca el número: "))
        numero_2 = str(input("Introduzca el siguiente número: "))
        operacion = str(operacion)
        mensaje = (operacion, numero_1, numero_2)
        mensaje = str(mensaje)
        mensaje=mensaje.replace("("," ").replace(")"," ")
        mensaje = ''.join(mensaje)
        serversocket.send(mensaje.encode())
        resultado = serversocket.recv(1024).decode()
        print("El resultado de la operación es: ", resultado)
    elif operacion ==0:
        sys.exit(1)

except socket.error:
    print("Ha habido un error con el socket")
