from socket import *

serverName = "localhost"
serverPort = 12000

def main():
	
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	while True:

		message = input("Input lowercase sentence:")

		if message == "exit":
			print("Connection terminated.")
			break

		clientSocket.sendto(message.encode(),(serverName, serverPort))

		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

		print("From server:", modifiedMessage.decode())

	clientSocket.close()

main()