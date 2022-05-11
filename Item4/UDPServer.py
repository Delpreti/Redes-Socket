from socket import *
import threading

serverPort = 12000

def attend_client(serverSocket, message, clientAddress):

	modifiedMessage = message.decode()

	print(modifiedMessage)

	#serverSocket.sendto(modifiedMessage.upper().encode(), clientAddress)

def main():

	serverSocket = socket(AF_INET, SOCK_DGRAM)

	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	serverSocket.bind(("", serverPort))

	print("The server is ready to receive")

	while True:

		message, clientAddress = serverSocket.recvfrom(2048)

		client = threading.Thread(target=attend_client, args=(serverSocket, message, clientAddress))

		client.start()

	serverSocket.close()

main()