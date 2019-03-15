import socket

IP = "10.0.2.15"
PORT = 8084

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

print("Read from the server", s.recv(2048).decode("utf-8")) 
