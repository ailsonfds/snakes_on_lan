from snake import Snake
from arena import Arena
try:
    from tkinter import Tk
    from tkinter.ttk import Button
except ImportError:
    from Tkinter import Tk, Button
    from ttk import Button
from time import sleep
from random import choice

class Mannager(object):
    """docstring for Mannager"""
    players={}
    players_colors={}

    def __init__(self, players_name=[], players_colors=[]):
        super(Mannager, self).__init__()
        self.players={}
        self.players_colors={}
        if len(players_name)!=len(players_colors):
            raise Exception("Aren't you missing someone?")
        for i, name in enumerate(players_name):
            self.players[name]=Snake()
            self.players_colors[name]=players_colors[i]

    def add_player(player_name, player_color, player_snake):
        self.players[player_name]=player_snake

    def score():
        score_dict={}
        for key, value in players.items():
            score_dict[key]=value.size*10
        return score_dict

def play(arena):
    p1_color='black'
    p1_name='player1'
    p1_snk=Snake(p1_color,[14,14])
    p1_snk.next_mov=choice([[-1,0],[1,0],[0,1],[0,-1]])
    Snake.xlims=29
    Snake.ylims=29
    arena.master.bind('<Up>', p1_snk.up)
    arena.master.bind('<Down>', p1_snk.down)
    arena.master.bind('<Left>', p1_snk.left)
    arena.master.bind('<Right>', p1_snk.right)
    arena.update_score({p1_name:p1_snk.size})
    for tile in p1_snk.loc:
        arena.draw_tile(tile[0],tile[1],p1_color)
    while arena.master.state()=='normal':
        msg, pos=p1_snk.move(p1_snk.next_mov[0],p1_snk.next_mov[1])
        if msg=='walk':
            arena.draw_tile(p1_snk.head[0],p1_snk.head[1],p1_color)
            arena.draw_tile(pos[0],pos[1],'white')
            arena.update()
        if 'crash' in msg:
            arena.lose_msg('P1 HAVE LOST')
            break
        sleep(1)

def main():
    root=Tk()
    ring=Arena(master=root,title='Snake Attack')
    root.protocol('WM_DELETE_WINDOW', ring.exit)
    ring.play_btn=Button(ring, text='PLAY')
    ring.play_btn['command']=lambda x=ring : play(x)
    ring.master.bind('<Return>', ring.play_btn['command'])
    ring.play_btn.grid(column=2, row=4)
    ring.mainloop()

if __name__ == '__main__':
    main()
