try:
    from tkinter import Tk, StringVar, Toplevel
    from tkinter.ttk import Button, Frame, Radiobutton
except ImportError:
    from Tkinter import Tk, StringVar, Toplevel
    from ttk import Button, Frame, Radiobutton
import random
import socket
import sys

from arena import Arena
from random import choice
from snake import Snake
from threading import Thread, Event
from time import sleep
import os
import signal


class Mannager(Arena):
    """
    docstring for Mannager

    This class is responsible for mannager each match.
    The purpose is to make this the server side of the main application.
    """
    port=5555
    host=''
    players={}
    players_colors={}
    players_score={}
    players_addrs={}
    __sckt = None
    __conn = {}
    __threads = {}
    __colors=['red', 'green', 'blue', 'yellow']
    food=[0,0]
    _game_on=False

    def __init__(self, master=None, title='Snake Attack', players_name=[], players_colors=[], lan_mode=False):
        super(Mannager, self).__init__(master, title)
        Snake.xlims=29
        Snake.ylims=29
        self.master.protocol('WM_DELETE_WINDOW', self.exit)
        self.port=5554
        self.host=''
        self.players={}
        self.players_colors={}
        self.players_score={}
        self.__sckt = None
        self.__conn = {}
        self.__threads = {}
        self.__colors=['red', 'green', 'blue', 'yellow']
        self.food=[0,0]
        self._game_on=True
        if len(players_name)!=len(players_colors):
            raise Exception("Aren't you missing someone?")
        for i, name in enumerate(players_name):
            self.players[name]=Snake(color=players_colors[i], initial_pos=[random.randint(0,29), random.randint(0,29)])
            self.players_colors[name]=players_colors[i]
            self.players_score[name]=self.players[name].size
        if len(players_name)==1:
            self.master.bind('<Up>', self.players[players_name[0]].up)
            self.master.bind('<Down>', self.players[players_name[0]].down)
            self.master.bind('<Left>', self.players[players_name[0]].left)
            self.master.bind('<Right>', self.players[players_name[0]].right)
        elif len(players_name)==2:
            self.master.bind('<Up>', self.players[players_name[0]].up)
            self.master.bind('<Down>', self.players[players_name[0]].down)
            self.master.bind('<Left>', self.players[players_name[0]].left)
            self.master.bind('<Right>', self.players[players_name[0]].right)
            self.master.bind('<w>', self.players[players_name[1]].up)
            self.master.bind('<s>', self.players[players_name[1]].down)
            self.master.bind('<a>', self.players[players_name[1]].left)
            self.master.bind('<d>', self.players[players_name[1]].right)
            # self.create_score({players_name[0]:self.players[players_name[0]].size, players_name[1]:self.players[players_name[1]].size})
        self.create_score(self.players_score)
        self.quit = Button(self, text="QUIT", command=self.exit)
        self.quit.grid(column=2, row=6)
        self.play_btn=Button(self, text='PLAY')
        self.play_btn.grid(column=2, row=4)
        self.play_thread=Thread(target=self.play)
        self.play_btn['command']=self.play_thread.start
        self.master.bind('<Return>', self.play_btn['command'])

        self.master.bind('<Control-c>', self.exit)
        self.master.bind('<Control-q>', self.exit)
        self.master.bind('<Alt-F4>', self.exit)
        self.master.bind('<Control-Escape>', self.exit)
        self.master.bind('<Escape>', self.exit)
        if lan_mode:
            self.connect_thread=Thread(target=self.connect)
            self.connect_thread.start()
            self.play_thread.start()

    def connect(self):
        """
        Method to check new connections and create new players
        """
        self.__sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__sckt.bind((self.host, self.port))
        while self._game_on:
            if not self._game_on:
                return
            print("[+] Listenning for connections at localhost:" + str(self.port))
            self.__sckt.listen(1)
            try:
                client, addr = self.__sckt.accept()
                ipaddr, port = addr
                addr = str(ipaddr) + ':' + str(port)
                self.__conn[addr] = client
                self.__threads[addr] = Thread(target= self.read, args=(addr,))
                self.__threads[addr].start()
                # print('Connected to ' + str(addr))
            except:
                print("Something gone wrong: " + str(e))

    def read(self, addr=''):
        while self._game_on:
            data = self.__conn[addr].recv(1024)
            if data:
                if 'left' in data:
                    self.players[self.players_addrs[addr]].left()
                elif 'right' in data:
                    self.players[self.players_addrs[addr]].right()
                elif 'up' in data:
                    self.players[self.players_addrs[addr]].up()
                elif 'down' in data:
                    self.players[self.players_addrs[addr]].down()
                elif 'name=' in data:
                    name=data.replace('name=','')
                    self.players_addrs[addr]=name
                    color=choice(self.__colors)
                    self.add_player(name,color,Snake(color=color, initial_pos=[random.randint(0,29), random.randint(0,29)]))
            print(data)

    def add_player(self,player_name, player_color, player_snake):
        self.players[player_name]=player_snake
        self.players_colors[player_name]=player_color
        self.players_score[player_name]=player_snake.size*10
        for snake_part in self.players[player_name].loc:
            self.draw_tile(snake_part[0],snake_part[1],self.players_colors[player_name])
        self.create_score(self.players_score)

    def score(self):
        score_dict ={}
        for key, value in self.players.items():
            score_dict[key]=value.size*10
            return score_dict

    def brew_food(self, randomP = False):
        xRandPos = 8
        yRandPos = 8
        if(randomP == True):
            xRandPos = random.randint(0, 29) ## Must respect the boundaries
            yRandPos = random.randint(0, 29)
        self.food[0] = xRandPos
        self.food[1] = yRandPos
        self.draw_tile(xRandPos,yRandPos,'black')
        self.update()
    
    def play(self):
        self.play_btn['command']=lambda x: y(x)
        self.brew_food(True)

        for key, value in self.players.items():
            for snake_part in value.loc:
                self.draw_tile(snake_part[0],snake_part[1],self.players_colors[key])
        self.update()
        while self._game_on:
            for key, player_i in self.players.items():
                player_color_i=self.players_colors[key]
                
                if((player_i.head[0] + player_i.next_mov[0] == self.food[0]) and (player_i.head[1] + player_i.next_mov[1] == self.food[1])):
                    msg, pos=player_i.move(player_i.next_mov[0],player_i.next_mov[1], growth=True)
                    self.players_score[key] = player_i.size
                elif(self.check_crash(key)):
                    msg, pos=player_i.move(player_i.next_mov[0],player_i.next_mov[1], crash=True)
                else:
                    msg, pos=player_i.move(player_i.next_mov[0],player_i.next_mov[1])
                
                if msg=='walk':
                    self.draw_tile(player_i.head[0],player_i.head[1],player_color_i)
                    self.draw_tile(pos[0],pos[1],'white')
                if msg == 'growth':
                    self.draw_tile(player_i.head[0],player_i.head[1],player_color_i)
                    self.brew_food(True)
                if 'crash' in msg:
                    self.lose_msg(key + '\nHAVE CRASHED')
                    return
                
                self.update()
                self.update_score(self.players_score)
                self.update_idletasks()
                sleep(0.1)

    def check_crash(self, player_name):
        player_head=self.players[player_name].head
        other_players=self.players.copy()
        del other_players[player_name]
        for key, value in other_players.items():
            if player_head in value.loc:
                return True
        return False

    def exit(self, *args):
        print("Closing Server...")
        self.game_on=False
        try:
            self.__sckt.close()
        except BaseException as e:
            print(e)
            pass
        print('pass')
        self.master.destroy()
        # os.kill(os.getpid(), signal.SIGINT)
    
def start(root, mode):
    root.destroy()
    root=Tk()
    if 'single' == mode:
        ring=Mannager(master=root,title='Snake Attack', players_name=['player1'], players_colors=['green'])
        ring.mainloop()
    elif '2' == mode:
        ring=Mannager(master=root,title='Snake Attack', players_name=['player1', 'player2'], players_colors=['green', 'red'])
        ring.mainloop()
    else:
        ring=Mannager(master=root,title='Snake Attack', lan_mode=True)
        ring.mainloop()

def main():
    root=Tk()
    mode=StringVar()
    start_screen=Frame(root, padding="12 12 12 12")
    root.title('Snack Attack')
    start_screen.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    start_screen.pack()
    Radiobutton(start_screen ,text='Local Single Mode', variable=mode, value="single").grid(row=1, column=1)
    Radiobutton(start_screen ,text='Local 2-Players Mode', variable=mode, value="2").grid(row=2, column=1)
    Radiobutton(start_screen ,text='Lan Multiplayer', variable=mode, value='lan').grid(row=3, column=1)
    Button(start_screen, text='START', command=lambda y=root, z=mode.get() : start(y,z)).grid(row=4, column=1)
    start_screen.mainloop()
    
if __name__ == '__main__':
    main()