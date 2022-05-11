from socket import *

serverName = "localhost"
serverPort = 12000

def main():
	
	clientSocket = socket(AF_INET, SOCK_STREAM)

	clientSocket.connect((serverName, serverPort))

	while True:

		message = input()

		clientSocket.send(message.encode())

		responseMessage = clientSocket.recv(2048).decode()

		print(responseMessage)

		if "Ate logo!" in responseMessage:
			break

	clientSocket.close()

main()