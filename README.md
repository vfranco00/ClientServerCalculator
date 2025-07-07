# Projeto Cliente-Servidor TCP em Python

Este projeto implementa uma aplicação simples de comunicação em rede utilizando **Sockets TCP em Python**, composta por dois arquivos principais: `Server.py` e `Client.py`.

O servidor aceita conexões de múltiplos clientes simultaneamente, permitindo que enviem comandos de **adição** ou **subtração**, e retorna o resultado da operação.

## Estrutura do Projeto
├── Client.py # Código do cliente TCP
├── Server.py # Código do servidor TCP com suporte a múltiplos clientes via threading
└── README.md # Este arquivo

## Como funciona

- O **cliente** se conecta ao servidor na porta 5555.
- O usuário insere um comando no seguinte formato:

adição 5 3
subtração 10 4.5

- O servidor interpreta o comando, executa a operação matemática e retorna o resultado.
- O comando `sair` encerra a conexão com o servidor.

## Execução

### 1. Inicie o servidor

```bash
python3 Server.py
```

A saída será algo como:
[SERVIDOR] Aguardando conexões...

### 2. Em outro terminal, inicie o cliente
```bash
python3 Client.py
```

### 3. Insira comandos no cliente
```bash
Digite a operação (adição/subtração) e dois números: adição 5 7
Servidor: Resultado: 12.0

Digite a operação (adição/subtração) e dois números: sair
Servidor: Conexão encerrada.
```

### Funcionalidades
Comunicação via TCP sockets

Multithreading no servidor para lidar com múltiplos clientes simultâneos

Validação de entrada e tratamento de erros

Operações básicas: adição e subtração

Requisitos
Python 3.x

Sistema operacional compatível com sockets (Linux, Windows, macOS)

### Aprendizados
Esse projeto é ideal para quem deseja aprender:

Comunicação cliente-servidor com Python

Uso da biblioteca socket

Manipulação de threads com threading

Tratamento básico de entrada/saída de dados entre aplicações

### Autores
Victor Eugênio Franco Magalhães Caetano
