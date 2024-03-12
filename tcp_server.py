import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = int(input("Informe a porta para a conexão TCP: "))

try:
    server.bind(("0.0.0.0",port))
    
    server.listen(5)
    print("Escutando para a conexão...")
    
    client_socket, address = server.accept()
    print("Conectado com o IP: " + address[0]) 
    
    while True:

        packets_received = client_socket.recv(100000).decode()
        print(f"Mensagem do cliente: {packets_received}")

        
        message_server = input("Mensagem do servidor: ") + "\n"
        client_socket.send(message_server.encode())

        if message_server == "Tchau\n" or "tchau\n":
            print(">>>>> A conexão foi finalizada.")
            break

except Exception as error:
    print(">>>>> Ocorreu erro ao realizar a conexão")
    print(error)
