import os
import sys
import socket
import threading
from colorama import Fore, Back, Style
os.system('cls')

# Global Variables
terminal_width = os.get_terminal_size().columns

host = '192.168.1.6'
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
		global nickname
		nickname = nickname_func()
		client_socket.connect((host, port))
		client_socket.send(nickname.encode('ascii'))
		nickname = client_socket.recv(1024).decode('ascii')
	except socket.error as msg:
		print("Connection Error: " + str(msg) + "\nRestart the Client and Try Again!")

# Take Nickname input

def nickname_func():
	print(Fore.GREEN + "Enter Your Alphanumeric Nickname: " + Style.RESET_ALL, end="")
	nickname = input()
	nickname.strip()
	if len(nickname) == 0 or len(nickname)>15 or nickname.isalnum() == False:
		print(Fore.RED + "Invalid Nickname" + Style.RESET_ALL)
		nickname_func()
	return nickname

# Receive Messages from the Server
def receive_messages():
	while True:
		try:
			message = client_socket.recv(20480).decode('ascii')
			if(message[0] != '@'):
				nn,msg = message.split(":",1)
				print(Fore.GREEN + nn + Fore.WHITE + ":" + msg + Style.RESET_ALL)
			else :
				print(Fore.YELLOW + message[1:] + Style.RESET_ALL)

		except KeyboardInterrupt:
			client_socket.close()
			sys.exit()	

		except:
			print("CHAT UP CLIENT ERROR CODE 002: Message Receiving Error!")
			client_socket.close()
			break

# Send Messages to the Server
def send_messages():
	try:
		while True:
			message = input()
			# sys.stdout.write("\033[F")  # Move cursor to the previous line
			# sys.stdout.write("\033[K")  # Clear the line
			# sys.stdout.flush()
			# print(Style.RESET_ALL)
			if len(message.strip()) == 0:
				continue
			client_socket.send(message.encode('ascii'))
	except KeyboardInterrupt:
			client_socket.close()
			sys.exit()	


# Running Threads
def run_threads():
	receive_thread = threading.Thread(target=receive_messages)
	receive_thread.start()

	send_thread = threading.Thread(target=send_messages)
	send_thread.start()

# Main function
def main():
	client_setup()
	connect_to_server()
	run_threads()

if __name__ == "__main__":
	main()