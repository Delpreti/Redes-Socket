from socket import *

serverName = "localhost"
serverPort = 12000

def main():
	
	clientSocket = socket(AF_INET, SOCK_STREAM)

	clientSocket.connect((serverName, serverPort))

	while True:

		username = input("username: ")
		password = input("password: ")
		message = f"{username} {password}"

		clientSocket.send(message.encode())

		responseMessage = clientSocket.recv(2048)

		print("From server:", responseMessage.decode())

	clientSocket.close()

main()