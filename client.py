import os
import socket
import threading

os.system('cls')

# Global Variables

terminal_width = os.get_terminal_size().columns

host = '192.168.1.4'
port = 55555
client_socket = None
nickname = ""

# Set up the Client by Creating a Socket Object
def client_setup():
	try:
		global client_socket
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as msg:
		print("Client side Socket Creation Error: " + str(msg) + "\nRetrying...")
		client_setup()

# Connect to the Server
def connect_to_server():
	try:
		client_socket.connect((host, port))
		client_socket.send(nickname.encode('ascii'))
	except socket.error as msg:
		print("Connection Error: " + str(msg) + "\nRetrying...")
		connect_to_server()

# Nickname
def nickname():
	global nickname
	nickname = input("Enter a Nickname: ")

# Receive Messages from the Server
def receive_messages():
	while True:
		try:
			message = client_socket.recv(1024).decode('ascii')
			print(message)
		except:
			print("An Error Occurred!")
			client_socket.close()
			break

# Send Messages to the Server
def send_messages():
	while True:
		msg = input()
		if len(msg.strip()) == 0:
			continue
		message = f"{nickname}: {msg}"
		client_socket.send(message.encode('ascii'))

# Running Threads
def run_threads():
	receive_thread = threading.Thread(target=receive_messages)
	receive_thread.start()

	send_thread = threading.Thread(target=send_messages)
	send_thread.start()

# Main function
def main():
	nickname()
	client_setup()
	connect_to_server()
	run_threads()

if __name__ == "__main__":
	main()