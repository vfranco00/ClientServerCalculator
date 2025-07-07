import socket
import threading

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    while True:
        try:
            data = conn.recv(1024).decode('utf-8')  # Recebe mensagem do cliente (máx 1024 bytes)
            if not data:
                break  # Se a mensagem for vazia, encerra a conexão

            if data.lower() == 'sair':
                conn.send("Conexão encerrada.".encode('utf-8'))
                break  # Encerra o loop e fecha a conexão

            # Espera receber a mensagem no formato: operacao numero1 numero2
            partes = data.split()
            if len(partes) != 3:
                conn.send("Formato inválido. Use: <adição|subtração> numero1 numero2".encode('utf-8'))
                continue  # Volta para esperar nova mensagem

            operacao, num1, num2 = partes

            try:
                num1 = float(num1)  # Tenta converter para número decimal
                num2 = float(num2)
            except ValueError:
                conn.send("Números inválidos.".encode('utf-8'))
                continue

            # Processa a operação pedida
            if operacao.lower() == 'adição':
                resultado = num1 + num2
            elif operacao.lower() == 'subtração':
                resultado = num1 - num2
            else:
                conn.send("Operação inválida. Use adição ou subtração.".encode('utf-8'))
                continue

            conn.send(f"Resultado: {resultado}".encode('utf-8'))  # Envia o resultado pro cliente
        except:
            break

    conn.close()
    print(f"[DESCONECTADO] {addr} desconectou.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))  # Escuta em todas as interfaces de rede
    server.listen()  # Começa a escutar conexões
    print("[SERVIDOR] Aguardando conexões...")

    while True:
        conn, addr = server.accept()  # Aceita nova conexão
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Cria thread pra lidar com o cliente
        thread.start()  # Inicia a thread
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")  # Conta threads ativas (menos a principal)

if __name__ == "__main__":
    start_server()
