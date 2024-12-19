import os
import socket
import threading
from queue import Queue

os.system('cls')

# Global Variables
host = '192.168.1.4'
port = 55555
server_socket = None

client_sockets = []
client_addresses = []
nicknames = []

# Set up the Server by Creating a Socket Object
def server_setup():
	try:
		global server_socket
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as msg:
		print("Server side Socket Creation Error: " + str(msg) + "\nRetrying...")
		server_setup()

# Binding the Server
def server_bind():
	try:
		print("Binding the Server to the Port: " + str(port))
		server_socket.bind((host, port))
		print("Bind Successful!")
		server_socket.listen()
	except socket.error as msg:
		print("Server side Socket Binding Error: " + str(msg))

# Accept Connections from Multiple Clientsb
def accept_connections():
	while True:
		client_socket, client_address = server_socket.accept()
		nickname = client_socket.recv(1024).decode('ascii')
		nicknames.append(nickname)
		client_sockets.append(client_socket)
		client_addresses.append(client_address)

		broadcast(f"{nickname} joined the chat!")

		thread = threading.Thread(target=handle_client, args=(client_socket,))
		thread.start()

# Handle Messages from Clients
def handle_client(client_socket):
	while True:
		try:
			message = client_socket.recv(1024).decode('ascii')
			broadcast(message)
		except:
			index = client_sockets.index(client_socket) # Remove the Client if disconnected
			nickname = nicknames[index]
			broadcast(f"{nickname} left the chat!")
			nicknames.remove(nickname)
			client_sockets.remove(client_socket)
			client_socket.close()
			break

def broadcast(message):
	print(message) # for server records
	for client_socket in client_sockets:
		client_socket.send(message.encode('ascii')) # for the clients

# Running Threads
def run_threads():
	accept_thread = threading.Thread(target=accept_connections)
	accept_thread.start()


# Main function
def main():
	server_setup()
	server_bind()
	run_threads()

if __name__ == "__main__":
	main()