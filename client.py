import os
import socket
import threading
from colorama import Fore, Back, Style
os.system('cls')

# Global Variables
terminal_width = os.get_terminal_size().columns

host = '192.168.1.2'
port = 9999
client_socket = None
nickname = ""

# Set up the Client by Creating a Socket Object
def client_setup():
	try:
		global client_socket
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as msg:
		print(Fore.RED + "Client side Socket Creation Error: " + Fore.LIGHTRED_EX + str(msg) + Fore.RED + "\nPLEASE RESTART YOUR CLIENT." + Style.RESET_ALL)

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
	try:
		nickname = input("Enter a Nickname: ")
		if len(nickname.strip()) == 0:
			print("Please Enter a Valid Nickname!")
			nickname()
	except:
		print("CHATUP CLIENT ERROR CODE 001: Nickname Error!")
		nickname()


# Receive Messages from the Server
def receive_messages():
	while True:
		try:
			sent_by_user = client_socket.recv(1024).decode('ascii')
			message = client_socket.recv(20480).decode('ascii')
			print(Fore.GREEN + sent_by_user +': '+ Fore.WHITE + message + Style.RESET_ALL)
		except:
			print("CHAT UP CLIENT ERROR CODE 002: Message Receiving Error!")
			client_socket.close()
			break

# Send Messages to the Server
def send_messages():
	while True:
		print(Fore.CYAN)
		message = input()
		print(Style.RESET_ALL)
		if len(message.strip()) == 0:
			continue
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