import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print(f'Falha na conexão! Error: {error}')
        sys.exit()

    print('Socket criado com succeso')
