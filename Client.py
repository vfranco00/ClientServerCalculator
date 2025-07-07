import socket

def start_client():
    """
    Função que inicia o cliente TCP para conectar ao servidor.

    O cliente envia comandos para o servidor no formato:
    "<adição|subtração> numero1 numero2"
    e recebe o resultado da operação.

    O cliente pode enviar 'sair' para encerrar a conexão.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Conecta no servidor local na porta 5555

    print("Conectado ao servidor. Digite 'sair' para encerrar.")
    while True:
        msg = input("Digite a operação (adição/subtração) e dois números: ")
        client.send(msg.encode('utf-8'))  # Envia a mensagem para o servidor

        resposta = client.recv(1024).decode('utf-8')  # Recebe resposta do servidor
        print(f"Servidor: {resposta}")

        if resposta == "Conexão encerrada.":
            break  # Sai do loop e encerra a conexão

    client.close()

if __name__ == "__main__":
    start_client()
