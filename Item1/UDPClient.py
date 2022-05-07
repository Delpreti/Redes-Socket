from socket import *

serverName = "localhost"
serverPort = 5000

def main():
	
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	while True:

		message = input("Input lowercase sentence:")

		if message == "exit":
			print("Connection terminated.")
			break

		clientSocket.sendto(message.encode(),(serverName, serverPort))

		if message == "end":
			print("Connection terminated.")
			break

		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

		print(modifiedMessage.decode())
	
	clientSocket.close()

main()