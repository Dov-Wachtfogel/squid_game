import socket
import digits4
from _thread import *

PORT = 12345


def client_handler(c, num: digits4.digits4):
    play = True
    rounds = 0
    while play:
        player_num = c.recv(32).decode()
        rounds += 1
        ans = num.check_num(player_num)
        if num.someone_win:
            play = False
            c.send('LOSE'.encode())
            c.close()
        if ans[:2] == '4A':
            play = False
            c.send('WON'.encode())
        elif rounds >= 10:
            play = False
            c.send('LOSE'.encode())
            c.close()
        else:
            c.send(ans.encode())


def accept_connections(ServerSocket, num):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, num))


def start_server():
    ServerSocket = socket.socket()
    num = digits4.digits4()
    try:
        ServerSocket.bind((PORT))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {PORT}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket, num)


if __name__ == '__main__':
    start_server()
