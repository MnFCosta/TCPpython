import socket
import struct

# criando um socket TCP (AF_INET indica a família de endereços IPV4 e SOCK_STREAM indica o protocolo TCP)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# configurando o endereço IP e a porta do servidor
endereco = ('localhost', 5000)
socket_tcp.bind(endereco)
# colocando o socket em modo de escuta
socket_tcp.listen()

print(f"Servidor rodando em {endereco}: Aguardando requisições...")

# loop que irá processar as conexões entrantes dos clientes
while True:
    # aguardando uma conexão de um cliente
    try:
        conexao, endereco_cliente = socket_tcp.accept()
        print(f"Conexão estabelecida com o cliente em {endereco_cliente}: Iniciando processamento...")
    except:
        print("Conexão falhou")
    
    
    # recebendo dados do cliente com um buffer máximo de 1024 bytes
    dados_recebidos = conexao.recv(1024)
    
    # processando os dados recebidos
    dados_processados = dados_recebidos[::-1].decode('utf-8') # invertendo a string
    
    # enviando a resposta de volta para o cliente
    data = struct.pack('!50s', dados_processados.encode('utf-8'))
    conexao.send(data)
    
    # fechando a conexão com o cliente atual
    conexao.close() 