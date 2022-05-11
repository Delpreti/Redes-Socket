from socket import *
import threading

serverPort = 12000

def attend_client(connectionSocket, clientAddress):

	_ = connectionSocket.recv(2048) # descartar mensagem inicial do usuario
	connectionSocket.send("Ola! Bem-vindo! Qual o seu nome?".encode())
	username = connectionSocket.recv(2048)

	options_string = f"Certo, {username.decode()}! Como posso te ajudar? Digite o numero que corresponde a opcao desejada:\n"
	options_string += "1. Agendar um horario de monitoria\n"
	options_string += "2. Listar as proximas atividades da disciplina\n"
	options_string += "3. E-mail do professor"
	connectionSocket.send(options_string.encode())

	message = connectionSocket.recv(2048)

	end_message = "Obrigado por utilizar nossos servicos!\nAte logo!"

	try:
		option = int(message.decode())
		if option not in [1, 2, 3]:
			raise ValueError
		if option == 1:
			connectionSocket.send(f"Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br \n{end_message}".encode())
		if option == 2:
			atividades = "P1: 26 de Maio de 2022\nLista3: 29 de Maio de 2022"
			connectionSocket.send(f"Fique atento para as datas das proximas atividades. Confira o que vem por ai!\n{atividades}\n{end_message}".encode())
		if option == 3:
			connectionSocket.send(f"Quer falar com o professor? o e-mail dele eh sadoc@dcc.ufrj.br \n{end_message}".encode())

	except:
		connectionSocket.send(end_message.encode())

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