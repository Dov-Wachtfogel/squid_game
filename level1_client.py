import socket

IP = '127.0.0.1'
PORT = 12345


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    play = True
    while play:
        num = str(input('enter a num to check: '))
        while len(num) != 4 and not num.isnumeric():
            num = str(input('enter a num to check: '))
        s.send(num.encode())
        ans = s.recv(128).decode()
        if ans == 'WON' or ans == 'LOSE':
            print('YOU ' + ans)
            play = False
        else:
            print(ans)
    s.close()


if __name__ == '__main__':
    main()
