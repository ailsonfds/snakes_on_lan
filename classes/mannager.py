# mannager.py
import snake
# import threading
import time

from arena import Arena
from random import randint

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


class Mannager:
    max_players = 3
    players_colors = ['red','green','blue']
    food_color='black'
    food_coord = [randint(0, 29), randint(0,29)]
    players = {}
    game_on=False

    def __init__(self, canvas=None):
        self.canvas=canvas
        self.add_player('player1')
        self.play_btn = ttk.Button(self.canvas.master, text="PLAY", command=self.single_player)
        self.play_btn.grid(column=2, row=5, sticky=(tk.W,tk.S))
        for child in self.canvas.master.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.canvas.master.master.bind('<Return>', self.single_player)
        

    def add_player(self,name=''):
        if len(self.players) <= self.max_players:
            self.players[name] = snake.Snake(color=self.players_colors[len(self.players.keys())])

    def single_player(self,*args):
        self.canvas.master.add_score_labels(self.players)
        self.canvas.create_rectangle(self.food_coord[0]*10,self.food_coord[1]*10,(self.food_coord[0]+1)*10,(self.food_coord[1]+1)*10,fill=self.food_color)
        key='player1'
        self.canvas.master.master.bind('<Key-Left>', self.players[key].walk_l)
        self.canvas.master.master.bind('<Key-Right>', self.players[key].walk_r)
        self.canvas.master.master.bind('<Key-Up>', self.players[key].walk_u)
        self.canvas.master.master.bind('<Key-Down>', self.players[key].walk_d)
        self.play_thread()

    def play_thread(self):
        key='player1'
        if self.game_on:
            raise Exception("Another match is running")
        self.game_on=True
        try:
            for coord in self.players[key].coords:
                x0=coord[0]*10
                y0=coord[1]*10
                x1=(coord[0]+1)*10
                y1=(coord[1]+1)*10
                self.canvas.create_rectangle(x0,y0,x1,y1,fill=self.players[key].color)
            # x0=self.players[key].head[0]*10
            # y0=self.players[key].head[1]*10
            # x1=(self.players[key].head[0]+1)*10
            # y1=(self.players[key].head[1]+1)*10
            # self.canvas.create_rectangle(x0,y0,x1,y1,fill=self.players[key].color)
            speed=2.0
            while self.game_on:
                value=self.canvas.master.score_value_label[key]
                value.config(text=self.players[key].score)
                # win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
                x0=self.players[key].coord[0]*10
                y0=self.players[key].coord[1]*10
                x1=(self.players[key].coord[0]+1)*10
                y1=(self.players[key].coord[1]+1)*10
                print(x0,y0,x1,y1)
                self.canvas.create_rectangle(x0,y0,x1,y1,fill='white')
                print(self.players[key].pattern,self.players[key].coord)
                if self.players[key].last == 'Left':
                    self.players[key].walk_l()
                if self.players[key].last == 'Right':
                    self.players[key].walk_r()
                if self.players[key].last == 'Down':
                    self.players[key].walk_d()
                if self.players[key].last == 'Up':
                    self.players[key].walk_u()
                if(self.players[key].pattern=='crash'):
                    break
                if(self.players[key].pattern=='food'):
                    self.canvas.create_rectangle(self.food_coord[0]*10,self.food_coord[1]*10,(self.food_coord[0]+1)*10,(self.food_coord[1]+1)*10,fill='white')
                    self.food_coord=self.players[key].coord
                    self.canvas.create_rectangle(self.food_coord[0]*10,self.food_coord[1]*10,(self.food_coord[0]+1)*10,(self.food_coord[1]+1)*10,fill=self.food_color)
                if(self.players[key].pattern=='pop'):
                    x0=self.players[key].coord[0]*10
                    y0=self.players[key].coord[1]*10
                    x1=(self.players[key].coord[0]+1)*10
                    y1=(self.players[key].coord[1]+1)*10
                    print(x0,y0,x1,y1)
                    self.canvas.create_rectangle(x0,y0,x1,y1,fill=self.players[key].color)
                time.sleep(speed/len(self.players[key].coords))
        except KeyboardInterrupt:
            self.exit()

    def play(self):
        self.game_on=True
        self.canvas.master.add_score_labels(self.players)
        while self.game_on:
            for key, value in self.canvas.master.score_value_label.items():
                value.set_text=self.players[key].score
                # win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
                x0=self.players[key].coords[0][0]*10
                y0=self.players[key].coords[0][1]*10
                x1=(self.players[key].coords[0][0]+1)*10
                y1=(self.players[key].coords[0][1]+1)*10
                print(x0,y0,x1,y1)
                if(self.players[key].pattern=='crash'):
                    break
                elif(self.players[key].pattern=='food'):
                    self.canvas.create_rectangle(self.food_coord[0]*10,self.food_coord[1]*10,(self.food_coord[0]+1)*10,(self.food_coord[1]+1)*10,fill='white')
                    self.food_coord=self.players[key].coord
                    self.canvas.create_rectangle(self.food_coord[0]*10,self.food_coord[1]*10,(self.food_coord[0]+1)*10,(self.food_coord[1]+1)*10,fill=self.food_color)

                self.canvas.create_rectangle(x0,y0,x1,y1,fill=self.players[key].color)
            time.sleep(5)

    def exit(self,*args):
        print("Finishing game...")
        self.game_on=False
        self.canvas.master.master.destroy()


def main():
    root = tk.Tk()
    app = Arena(master=root,title='Snake Attack')
    # app.pane.create_rectangle(20,20,30,30,fill='red')
    mannager = Mannager(app.pane)
    print(mannager)
    app.mainloop()

if __name__ == "__main__":
    main()
