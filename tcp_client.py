import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip = input("Informe o IP para a conexão TCP: ")
port = int(input("Informe a porta para a conexão TCP: "))

try:
    client.connect((ip, port))

    while True:
        message = input("Mensagem do cliente: ") + "\n"
        client.send(message.encode())


        packets_received = client.recv(100000).decode()
        print(f"Mensagem do servidor: {packets_received}")

        if message == "Tchau\n" or "tchau\n":
            print(">>>>> A conexão foi finalizada.")
            break

except Exception as error:
    print(">>>>> Ocorreu erro ao realizar a conexão")
    print(error)


