import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 12345))

server_socket.listen(5)

print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

folder_name = client_socket.recv(1024).decode('utf-8')

if os.path.exists(folder_name):
    client_socket.send(folder_name.encode('utf-8'))
    
    files = os.listdir(folder_name) 
    
    num_files_bytes = len(files).to_bytes(4, byteorder='big')
    client_socket.send(num_files_bytes)

    for file_name in files:
        client_socket.send(file_name.encode('utf-8'))
        
        with open(os.path.join(folder_name, file_name), 'rb') as file:
            chunk = file.read(1024)
            while chunk:
                client_socket.send(chunk)
                chunk = file.read(1024)
    print(f"Folder '{folder_name}' sent successfully.")
else:
    print(f"Folder '{folder_name}' does not exist on the server.")

client_socket.close()
server_socket.close()
