import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("You are all set to connect Saurabh Gawali's Device")
client_socket.connect(('192.168.25.27', 12345))  

file_name = "gate.txt"

client_socket.send(file_name.encode('utf-8'))

with open('got.txt', 'wb') as file:
    chunk = client_socket.recv(1024)
    while chunk:
        file.write(chunk)
        chunk = client_socket.recv(1024)
print("File received and saved")

client_socket.close()
