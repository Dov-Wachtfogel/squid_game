import socket
import digits4

PORT = 12345


def main():
    s = socket.socket()
    s.bind(('', PORT))
    s.listen(5)
    while True:
        c, addr = s.accept()
        play = True
        num = digits4.digits4()
        rounds = 0
        while play:
            player_num = c.recv(32).decode()
            rounds += 1
            ans = num.check_num(player_num)
            if ans[:2] == '4A':
                play = False
                c.send('WON'.encode())
                c.close()
            elif rounds <= 10:
                play = False
                c.close()
                c.send('LOSE'.encode())
            else:
                c.send(ans.encode())


if __name__ == '__main__':
    main()
