from socket import *

serverName = "localhost"
serverPort = 5001

def main():
	
	clientSocket = socket(AF_INET, SOCK_STREAM)

	clientSocket.connect((serverName, serverPort))

	while True:

		message = input("Input lowercase sentence:")

		if message == "exit":
			print("Connection terminated.")
			break

		clientSocket.send(message.encode())

		if message == "end":
			print("Connection terminated.")
			break

		modifiedMessage = clientSocket.recv(2048)

		print("From server:", modifiedMessage.decode())

	clientSocket.close()

main()