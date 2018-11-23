import socket
import sys
import time
try:
    from tkinter import Tk
    from tkinter.ttk import Button
except ImportError:
    from Tkinter import Tk, Button
    from ttk import Button

class Client:

    host = 'localhost'    # The remote host
    port = 57596              # The same port as used by the server
    __sckt = None


    def __init__(self, host = 'localhost', port=0):
        self.host=host
        self.port=port


    def connect(self):
        try:
            print("Trying make connection on: "+ self.host + ":" + str(self.port) + "...\n\n")
            self.__sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sckt.connect((self.host , self.port))
            self.send()

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
        print("Suscefully connection")
        while True:
            try:
                msg = input()
                self.__sckt.sendall(bytes(msg))
                # msg = self.__sckt.recv(1024).strip("\n")
                # if msg == "Ok":
                    # print(msg)
                    # self.connect()

            except socket.error as e:
                print("Error receiving data: " + str(e))
                self.__sckt.send(str(e))
                self.__sckt.close()
                self.connect()

    def close(self):
        self.__sckt.close()


def main():
    ip = 'localhost'
    port = 5554
    if(len(sys.argv) > 2):
        ip = sys.argv[1]
        port = int(sys.argv[2])
    client = Client(ip, port)
    try:
        client.connect()
        name='ailson'
        data='name='+name
        client.send(msg=data)
        while True:
            data=
            client.send(msg=data)

    except KeyboardInterrupt:
        print("\n\nFinishing aplication...")
        client.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
