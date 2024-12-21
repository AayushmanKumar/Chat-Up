import os
import socket
import threading
from queue import Queue
from colorama import Fore, Back, Style

os.system('cls')

# Global Variables
host = '192.168.1.2'
port = 9999
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
		print(Fore.RED + "Server side Socket Creation Error: " + Fore.LIGHTRED_EX + str(msg) + Fore.RED + "\nPLEASE RESTART THE SERVER." + Style.RESET_ALL)

# Binding the Server
def server_bind():
	try:
		print("Binding the Server to the Port: " + str(port))
		server_socket.bind((host, port))
		print("Bind Successful!")
		server_socket.listen()
	except socket.error as msg:
		print(Fore.RED + "Server side Socket Binding Error: " + Fore.LIGHTRED_EX + str(msg) + Fore.RED + "\nPLEASE CHECK THE CONFIGURATION AND RESTART THE SERVER." + Style.RESET_ALL)

# Accept Connections from Multiple Clientsb
def accept_connections():
	while True:
		client_socket, client_address = server_socket.accept()
		nickname = client_socket.recv(1024).decode('ascii')
		nicknames.append(str(nickname + " @ " + str(client_address[0])))
		client_sockets.append(client_socket)
		client_addresses.append(client_address)
		broadcast_name(nickname)
		broadcast_message("joined the chat!")

		thread = threading.Thread(target=handle_client, args=(client_socket,))
		thread.start()

# Handle Messages from Clients
def handle_client(client_socket):
	while True:
		try:
			
			message = client_socket.recv(20480).decode('ascii')
			broadcast_name(nicknames[client_sockets.index(client_socket)])
			broadcast_message(message)
		except:
			index = client_sockets.index(client_socket) # Remove the Client if disconnected
			nickname = nicknames[index]
			broadcast_name(nickname)
			broadcast_message("left the chat!")
			nicknames.remove(nickname)
			client_sockets.remove(client_socket)
			client_socket.close()
			client_addresses.remove(client_addresses[index])
			break

def broadcast_name(nickname):
	print(Fore.GREEN + nickname + ": " + Style.RESET_ALL,end ="") # for server records
	for client_socket in client_sockets:
		client_socket.send(nickname.encode('ascii')) # for

def broadcast_message(message):
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