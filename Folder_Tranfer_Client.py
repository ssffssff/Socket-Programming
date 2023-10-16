import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("You are all set to connect Saurabh Gawali's Device")

client_socket.connect(('192.168.25.27', 12345))  

folder_name = "Bhimashankar"

client_socket.send(folder_name.encode('utf-8'))

received_folder_name = client_socket.recv(1024).decode('utf-8')

if not os.path.exists(received_folder_name):
    os.mkdir(received_folder_name)

num_files_bytes = client_socket.recv(4)

num_files = int.from_bytes(num_files_bytes, byteorder='big')

for _ in range(num_files):
    file_name = client_socket.recv(1024).decode('utf-8')

    with open(os.path.join(received_folder_name, file_name), 'wb') as file:
        chunk = client_socket.recv(1024)
        while chunk:
            file.write(chunk)
            chunk = client_socket.recv(1024)

print(f"Folder '{received_folder_name}' received and saved on the client side.")

client_socket.close()