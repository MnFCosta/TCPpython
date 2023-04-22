import socket
import struct

# criando um socket TCP (AF_INET indica a família de endereços IPV4 e SOCK_STREAM indica o protocolo TCP)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# configurando o endereço IP e a porta do servidor
endereco = ('localhost', 5000)

# configurando o endereço IP e a porta do cliente2
endereco_cliente = ('localhost', 5002)
socket_tcp.bind(endereco_cliente)

# conectando-se ao servidor
socket_tcp.connect(endereco)

# enviando dados para o servidor utilizando a biblioteca "struct"
# a struct empacota a string enviada (dado que desejamos processar no servidor) em um objeto de 50 bytes
#para que ela possa ser enviada para o servidor
input = input("Digite alguma coisa: ")
dado = struct.pack('!50s', input.encode('utf-8'))
socket_tcp.send(dado)

# recebendo a resposta do servidor utilizando o método recv do socket
dados_recebidos = socket_tcp.recv(1024)

# processando a resposta do servidor utilizando o decode para 
# decodificar uma sequencia de bytes recebidas pelo servidor em
# uma string legível
resposta = dados_recebidos.decode('utf-8')

print('Resultado do processamento: ', resposta)

# fechando o socket
socket_tcp.close()