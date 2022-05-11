from socket import *
import threading

serverPort = 12000

username = "usuario"
password = "senha"

def attend_client(connectionSocket, clientAddress):

	while True:

		message = connectionSocket.recv(2048)

		if not message:

			print(str(clientAddress) + " has requested to end his session.")

			connectionSocket.close()

			return

		credentials = message.decode().split()

		if len(credentials) != 2:
			connectionSocket.send("Error: client message is not formatted properly".encode())
		elif (credentials[0] == username) and (credentials[1] == password):
			connectionSocket.send("Success!".encode())
		else:
			connectionSocket.send("Error: invalid credentials".encode())

def main():

	serverSocket = socket(AF_INET, SOCK_STREAM)

	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	serverSocket.bind(("", serverPort))

	serverSocket.listen(5)

	print("The server is ready to receive")

	while True:

		client = threading.Thread(target=attend_client, args=serverSocket.accept())

		client.start()

	serverSocket.close()

main()