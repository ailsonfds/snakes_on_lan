import socket
import sys
import threading
# import time
import argparse
import subprocess
# Thanks to https://stackoverflow.com/questions/12332975/installing-python-module-within-code
try:
    import pyautogui
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'python3-xlib'])
    subprocess.call([sys.executable, "-m", "pip", "install", 'pyautogui'])
finally:
    import importlib
    globals()['pyautogui'] = importlib.import_module('pyautogui')


exitFlag = 0

class Server:

    host = ''
    port = 0
    __sckt = None
    __conn = {}
    __threads = {}

    def __init__(self, port=0):
        self.port = port
        try:
            self.__sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__sckt.bind((self.host, self.port))
            self.__sckt.listen(100)
        except socket.error as e:
            print("Error while creating socket: " + str(e))

    def connect(self):
        print("[+] Listenning for connections")
        while True:
            try:
                client, addr = self.__sckt.accept()
                ipaddr, port = addr
                addr = str(ipaddr) + ':' + str(port)
                self.__conn[addr] = client
                self.__threads[addr] = threading.Thread(target= self.read, args=(addr,))
                self.__threads[addr].start()
                print('Connected to ' + str(addr))
            except socket.error as e:
                print("Something gone wrong: " + str(e))

    def read(self, addr=''):
        while True:
            data = self.__conn[addr].recv(1024)
            if not data:
                break
            print(str(data,'utf-8'))
            pyautogui.press(str(data,'utf-8').strip('\n'))
            self.__conn[addr].send(bytes('Ok','utf-8'))
            return data

    def close(self):
        if self.__sckt:
            self.__sckt.close()


def main():
    arg = argparse.ArgumentParser(description="Servidor")
    arg.add_argument("--port", dest="port", type=int, default=50007, help="porta")

    if (len(sys.argv) < 1):
        arg.print_help()
        sys.exit(1)

    args = arg.parse_args()
    port = args.port
    #i = 1

    try:
        server = Server(port)
        server.connect()
    except KeyboardInterrupt:
        print("Closing Server...")
        server.close()
        sys.exit(0)


if __name__ == "__main__":
    main()
