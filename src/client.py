import socket
import sys
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

    def on_press(key):
        if key == Key.left:
            self.send(msg='left')
        elif key == Key.right:
            self.send(msg='right')
        elif key == Key.up:
            self.send(msg='up')
        elif key == Key.down:
            self.send(msg='down')

    def on_release(key):
        if key == Key.esc:
            # Stop listener
            return False

def main():
    ip = 'localhost'
    port = 5554
    if(len(sys.argv) > 2):
        ip = sys.argv[1]
        port = int(sys.argv[2])
    client = Client(ip, port)
    root=Tk()
    try:
        client.connect()
        name='ailson'
        data='name='+name
        client.send(msg=data)
        # Collect events until released
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
        # root.bind('<Up>', client.send_up)
        # root.bind('<Down>', client.send_down)
        # root.bind('<Left>', client.send_left)
        # root.bind('<Right>', client.send_right)
        while True:
            client.send(msg='')

    except KeyboardInterrupt:
        print("\n\nFinishing aplication...")
        client.close()
        sys.exit(1)

if __name__ == "__main__":
    main()