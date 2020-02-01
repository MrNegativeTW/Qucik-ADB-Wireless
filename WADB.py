import subprocess
from time import sleep


def initAsk(choice):
    if choice == '1':
        connect()
    elif choice == '2':
        disconnect()


def connect():
    print('[Info] Connecting...')
    print(subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE).stdout.decode('utf-8'), end='')

    print(subprocess.run(['adb', 'tcpip', '5555'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

    print('[Info] Enter deviece ip or 0(same as last time): ', end='')
    userInput = input()
    if userInput == '0':
        userInput = getLastTimeIp()
    else:
        f = open('LastIP.txt', 'w')
        f.write(userInput)
        f.close()

    print(subprocess.run(['adb', 'connect', userInput + ':5555'], stdout=subprocess.PIPE).stdout.decode('utf-8'))


def disconnect():
    print(subprocess.run(['adb', 'disconnect'], stdout=subprocess.PIPE).stdout.decode('utf-8'), end='')

    print('[Info] Plug-in usb cable in 10 sec.')
    sleep(10)

    print(subprocess.run(['adb', 'usb'], stdout=subprocess.PIPE).stdout.decode('utf-8'), end='')


def getLastTimeIp():
    f = open("LastIP.txt", "r")
    ip = f.readline()
    return str(ip)


if __name__ == '__main__':
    print('1: Connect, 2: Disconnect, What do you want? ', end="")
    initAsk(input())