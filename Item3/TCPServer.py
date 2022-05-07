from socket import *
import threading

serverPort = 12000

def attend_client(connectionSocket, clientAddress):

	while True:

		message = connectionSocket.recv(2048)

		if not message:

			print(str(clientAddress) + " has requested to end his session.")

			connectionSocket.close()

			return

		connectionSocket.send(message.decode().upper().encode())


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