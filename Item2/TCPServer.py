from socket import *

serverPort = 5001

def main():

	serverSocket = socket(AF_INET, SOCK_STREAM)

	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	serverSocket.bind(("", serverPort))

	serverSocket.listen(5)

	print("The server is ready to receive")

	# persistente
	connectionSocket, clientAddress = serverSocket.accept()

	while True:
		
		message = connectionSocket.recv(2048).decode()

		if message == "end":
			print("Server shutdown requested by the client.")
			connectionSocket.close()
			break

		connectionSocket.send(message.upper().encode())

	connectionSocket.close()

	serverSocket.close()

main()