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
import random


class Mannager(Arena):
	"""
	docstring for Mannager

	This class is responsible for mannager each match.
	The purpose is to make this the server side of the main application.
	"""
	players={}
	players_colors={}
	food=[0,0]

	def __init__(self, players_name=[], players_colors=[]):
		super(Mannager, self).__init__()
		self.players={}
		self.players_colors={}
		self.food=[]
		if len(players_name)!=len(players_colors):
			raise Exception("Aren't you missing someone?")
		for i, name in enumerate(players_name):
			self.players[name]=Snake()
			self.players_colors[name]=players_colors[i]

	def add_player(self,player_name, player_color, player_snake):
		self.players[player_name]=player_snake
		self.players_colors[player_name]=player_color

	def score(self):
		score_dict ={}
		for key, value in self.players.items():
			score_dict[key]=value.size*10
			return score_dict

	def brew_food(self, randomP = False):
		xRandPos = 8
		yRandPos = 8
		if(randomP == True):
			xRandPos = random.randint(0, 100)
			yRandPos = random.randint(0, 100)

			food[0] = xRandPos
			food[1] = yRandPos		
		self.draw_tile(xRandPos,yRandPos,'red')
		self.update()
	
	def play(self):
		Snake.xlims=29
		Snake.ylims=29
		
		for key in players:
			player_i = players[key]
			for tile in player_i.loc:
				self.draw_tile(tile[0],tile[1],p1_color)
		
		while self.master.state()=='normal':
			players_score = {}
			for key in players:
				player_i = players[key]
				player_color_i = players_colors[key]

				if((player_i.head[0] + next_mov[0] == food[0]) and (player_i.head[1] + next_mov[1] == food[1])):
					msg, pos=player_i.move(player_i.next_mov[0],player_i.next_mov[1], True)				
				else:
					msg, pos=player_i.move(player_i.next_mov[0],player_i.next_mov[1])
				if msg=='walk':					
					self.draw_tile(player_i.head[0],player_i.head[1],player_color_i)					
					self.draw_tile(pos[0],pos[1],'white')
					self.update()
				if msg == 'growth':					
					self.draw_tile(player_i.head[0],player_i.head[1],player_color_i)
					self.brew_food(self, True)
					self.update()
				if 'crash' in msg:
					self.lose_msg(key + ' HAVE\nCRASHED')
					break
				players_score[key] = player_i.size
			self.update_score(players_score)
			sleep(0.1)			

def play(arena):
	food = [0,0]
	
	def brew_food(arena, randomP = False):
		xRandPos = 8
		yRandPos = 8
		if(randomP == True):
			xRandPos = random.randint(0, 100)
			yRandPos = random.randint(0, 100)

			food[0] = xRandPos
			food[1] = yRandPos		
		arena.draw_tile(xRandPos,yRandPos,'red')
		arena.update()

	Snake.xlims=29
	Snake.ylims=29

	p1_color='black'
	p1_name='player1'
	p1_snk=Snake(color=p1_color,initial_pos=[14,14])
	p1_snk.next_mov=choice([[-1,0],[1,0],[0,1]])
	
	p2_color='green'
	p2_name='player2'
	p2_snk=Snake(color=p2_color,initial_pos=[24,24])
	p2_snk.next_mov=choice([[-1,0],[1,0],[0,1]])
   
	arena.master.bind('<Up>', p1_snk.up)
	arena.master.bind('<Down>', p1_snk.down)
	arena.master.bind('<Left>', p1_snk.left)
	arena.master.bind('<Right>', p1_snk.right)
	arena.master.bind('<w>', p2_snk.up)
	arena.master.bind('<s>', p2_snk.down)
	arena.master.bind('<a>', p2_snk.left)
	arena.master.bind('<d>', p2_snk.right)
	arena.create_score({p1_name:p1_snk.size, p2_name:p2_snk.size})

	brew_food(arena, True)

	for tile in p1_snk.loc:
		arena.draw_tile(tile[0],tile[1],p1_color)
	for tile in p2_snk.loc:
		arena.draw_tile(tile[0],tile[1],p1_color)

	while arena.master.state()=='normal':
		if((p1_snk.head[0] + p1_snk.next_mov[0] == food[0]) and (p1_snk.head[1] + p1_snk.next_mov[1] == food[1])):
			msg, pos=p1_snk.move(p1_snk.next_mov[0],p1_snk.next_mov[1], True)				
		else:
			msg, pos=p1_snk.move(p1_snk.next_mov[0],p1_snk.next_mov[1])

		if msg=='walk':
			arena.draw_tile(p1_snk.head[0],p1_snk.head[1],p1_color)
			arena.draw_tile(pos[0],pos[1],'white')
			arena.update()
		if msg=='growth':
			arena.draw_tile(p1_snk.head[0],p1_snk.head[1],p1_color)
			brew_food(arena, True)
			arena.update()
		if 'crash' in msg:
			arena.lose_msg('P1 HAVE\nSELF\nCRASHED')
			break
	
		if((p2_snk.head[0] + p2_snk.next_mov[0] == food[0]) and (p2_snk.head[1] + p2_snk.next_mov[1] == food[1])):
			msg, pos=p2_snk.move(p2_snk.next_mov[0],p2_snk.next_mov[1], True)				
		else:
			msg, pos=p2_snk.move(p2_snk.next_mov[0],p2_snk.next_mov[1])
		if msg=='walk':
			arena.draw_tile(p2_snk.head[0],p2_snk.head[1],p2_color)
			arena.draw_tile(pos[0],pos[1],'white')
			arena.update()
		if msg=='growth':
			arena.draw_tile(p2_snk.head[0],p2_snk.head[1],p2_color)
			brew_food(arena, True)
			arena.update()
		if 'crash' in msg:
			arena.lose_msg('P2 HAVE\nSELF\nCRASHED')
			break
		arena.update_score({p1_name:p1_snk.size, p2_name:p2_snk.size})
		sleep(0.1)

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
