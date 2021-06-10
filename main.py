import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print(f'Falha na conexão! Error: {error}')
        sys.exit()

    print('Socket criado com succeso')


    # Definir o host que vai ser conectado

    hostuser = input('Digite o host ou ip a ser conectado: ')
    portuser = input('Digite a porta a ser conectada: ')

    try:
        s.connect((hostuser, int(portuser)))
        print(f'Cliente TCP Conectado com sucesso no Host: {hostuser}, na porta: {portuser}')
        s.shutdown(2)  # Espera dois segundos para finalizar a execução
    except socket.error as error:
        print(f'Não foi possível se conectar ao Host. Erro: {error}')
        sys.exit()


main()
