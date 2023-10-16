import socket
import os
from datetime import datetime
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 12345))

server_socket.listen(5)

print("Hello there! My name is Saurabh Subhash Gawali")
print("Server is waiting for a connection...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")
dt1 = datetime.now()
file_name = client_socket.recv(1024).decode('utf-8')

if os.path.exists(file_name):
    with open(file_name, 'rb') as file:
        chunk = file.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = file.read(1024)
    print(f"File '{file_name}' sent successfully.")
else:
    print(f"File '{file_name}' does not exist on the server.")
dt2 = datetime.now()
print((dt2 - dt1)/1e-9)
client_socket.close()
server_socket.close()