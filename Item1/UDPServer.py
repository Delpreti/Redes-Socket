from socket import *

serverPort = 5000

def main():

	serverSocket = socket(AF_INET, SOCK_DGRAM)

	serverSocket.bind(("", serverPort))

	print("The server is ready to receive")

	while True:
		
		message, clientAddress = serverSocket.recvfrom(2048)

		modifiedMessage = message.decode()

		if modifiedMessage.lower() == "end":
			print("Server shutdown requested by the client.")
			break

		serverSocket.sendto(modifiedMessage.upper().encode(), clientAddress)

main()