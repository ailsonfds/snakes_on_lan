import socket
import sys
import argparse
import time
from pynput.keyboard import Key, Listener
try:
    from tkinter import Tk
except ImportError:
    from Tkinter import Tk

class Client:

    host = 'localhost'    # The remote host
    port = 57596          # The same port as used by the server
    __sckt = None


    def __init__(self, host = 'localhost', port=0):
        self.host=host
        self.port=port


    def connect(self):
        try:
            print("Trying make connection on: "+ self.host + ":" + str(self.port) + "...\n\n")
            self.__sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sckt.connect((self.host , self.port))

        except socket.gaierror as e:
            print("Unknow Host: %s" %e)
            print("Sleeping 3 seconds before try again...\n")
            time.sleep(3)
            self.connect()

        except socket.error as e:
            print("connection error: %s" %e)
            print("Sleeping 3 seconds before try again...\n")
            time.sleep(3)
            self.connect()

    def send(self, msg='Foo'):
        try:
            print(msg)
            self.__sckt.sendall(bytes(msg))
        except socket.error as e:
            print("Error receiving data: " + str(e))
            self.__sckt.send(str(e))
            self.__sckt.close()
            self.connect()


    def send_left(self):
        self.send(msg='left')

    def send_right(self):
        self.send(msg='right')

    def send_up(self):
        self.send(msg='up')

    def send_down(self):
        self.send(msg='down')

    def close(self):
        self.__sckt.close()

    def on_press(self, key):
        if key == Key.left:
            self.send(msg='left')
        elif key == Key.right:
            self.send(msg='right')
        elif key == Key.up:
            self.send(msg='up')
        elif key == Key.down:
            self.send(msg='down')

    def on_release(self, key):
        if key == Key.esc:
            # Stop listener
            return False

def main():

    arg = argparse.ArgumentParser(description="Servidor")
    arg.add_argument("--name", dest="name", type=str, default='test', help="nome")
    arg.add_argument("--port", dest="port", type=int, default=5554, help="porta que o servidor escuta")
    arg.add_argument("--ip", dest="ip", type=str, default='localhost', help="endereco ip do servidor")

    if (len(sys.argv) < 1):
        arg.print_help()
        sys.exit(1)

    args = arg.parse_args()
    port = args.port
    ip=args.ip
    name=args.name

    client = Client(ip, port)
    root=Tk()
    try:
        client.connect()
        data='name='+name
        client.send(msg=data)
        # Collect events until released
        with Listener(
                on_press=client.on_press,
                on_release=client.on_release) as listener:
            listener.join()
        while True:
            client.send(msg='')

    except KeyboardInterrupt:
        print("\n\nFinishing aplication...")
        client.close()
        sys.exit(1)

if __name__ == "__main__":
    main()