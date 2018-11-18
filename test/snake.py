from random import randint, choice
from src.snake import Snake
import time

def check_borders(loc):
	if loc[0] < 0:
		loc[0]=Snake.xlims
	if loc[0] > Snake.xlims:
		loc[0]=0
	if loc[1] < 0:
		loc[1]=Snake.ylims
	if loc[1] > Snake.ylims:
		loc[1]=0


def main():
	snk1=Snake('blue')
	loc1=[[0,2],[0,1],[0,0]]
	snk2=Snake('red',[2,4])
	loc2=[[2,6],[2,5],[2,4]]
	x, y=randint(0,10), randint(0,8)
	snk3=Snake('blue',[x, y])
	loc3=[[x,y+2],[x,y+1],[x,y]]
	snk3_traceback=[]
	i=0
	while i<10:
		i=i+1
		if snk1.alive:
			assert snk1.loc==loc1, "%r != %r" %(snk1.loc,loc1)
			msg1, pos=snk1.move()
			loc1.insert(0,[loc1[0][0]+0,loc1[0][1]+1])
			if 'walk' in msg1:
				check_borders(loc1[0])
			loc1.pop()
		if snk2.alive:
			assert snk2.loc==loc2, "%r != %r" %(snk2.loc,loc2)
			msg2, pos=snk2.move(1,0)
			loc2.insert(0,[loc2[0][0]+1,loc2[0][1]+0])
			if 'walk' in msg2:
				check_borders(loc2[0])
			loc2.pop()
		if snk3.alive:
			assert snk3.loc==loc3, "%r != %r" %(snk3.loc,loc3)
			x, y=choice([1,0,-1]), choice([1,0,-1])
			while (x, y)==(0, 0) or (x, y)==(1, 1) or (x, y)==(-1, 1) or (x, y)==(1, -1) or (x, y)==(-1, -1):
				x, y=choice([1,0,-1]), choice([1,0,-1])
			msg3, pos=snk3.move(x,y,choice([True,False,False,False]))
			snk3_traceback.append(((x,y),msg3))
			loc3.insert(0,[loc3[0][0]+x,loc3[0][1]+y])
			if 'walk' in msg3 or 'growth' in msg3:
				check_borders(loc3[0])
			if 'growth'!=msg3:
				loc3.pop()
		# print(i, 'snk1 ' + msg1 + '. Is alive? ' + str(snk1.alive), '. snk2 ' + msg2 + '. Is alive? ' + str(snk2.alive), '. snk3 ' + msg3 + '. Is alive? ' + str(snk3.alive) + '.')
		# time.sleep(1)
	print('Snake 1 final location: ' + str(snk1.loc))
	print('Snake 2 final location: ' + str(snk2.loc))
	print('Snake 3 final location: ' + str(snk3.loc))
	print('Snake 3 traceback: ' + str(snk3_traceback))
	return

if __name__ == '__main__':
	main()
