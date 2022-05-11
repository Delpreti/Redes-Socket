from socket import *

serverName = "localhost"
serverPort = 12000
N = 20

def main():
	
	clientSocket = socket(AF_INET, SOCK_STREAM)

	clientSocket.connect((serverName, serverPort))

	i = 0

	while i < N:

		message = str(i)

		clientSocket.send(message.encode())

		#modifiedMessage = clientSocket.recv(2048)

		#print("From server:", modifiedMessage.decode())

		i += 1

	clientSocket.close()

main()