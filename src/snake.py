class Snake(object):
	"""docstring for Snake"""
	loc=[]
	head=[]
	tail=[]
	color=None
	size=len(loc)
	next_mov=[0,1]
	alive=True
	## Border superior limits. The inferor limite is aways 0, so we don't have to worry about it.
	_xlims=10
	_ylims=10
	_initial_size=3

	def __init__(self, color, initial_pos=[0,0]):
		super(Snake, self).__init__()
		self.loc=[]
		self.head=[]
		self.tail=[]
		self.color=color
		self.next_mov=[0,1]
		self.alive=True
		self.loc.append(initial_pos)
		self.update()
		# print(color)
		while self.size < self._initial_size:
			self.move(growth=True)

	def get_xlims(self):
		return type(self)._xlims

	def set_xlims(self,xlims):
		type(self)._xlims=xlims

	xlims=property(get_xlims, set_xlims)

	def get_ylims(self):
		return type(self)._ylims

	def set_ylims(self,ylims):
		type(self)._ylims=ylims

	ylims=property(get_ylims, set_ylims)

	def get_initial_size(self):
		return type(self)._initial_size

	def set_initial_size(sel,size):
		## Making shure if it's a valid size
		try:
			if size<0 and not isinstance(size, int):
				raise Exception('Not a valid value. Try a positive integer.')
		except:
			if size<0 and not isinstance(size, (int, long)): ## If running on python 2.x
				raise Exception('Not a valid value. Try a positive integer.')
		type(self)._initial_size=size

	initial_size=property(get_initial_size, set_initial_size)

	def update(self):
		self.head=self.loc[0]
		self.tail=self.loc[-1]
		self.size=len(self.loc)

	def move(self,xcoord=next_mov[0],ycoord=next_mov[1],growth=False):
		'''
		To move down set ycoord=1.
		To move up set ycoord=-1.
		To move right set xcoord=1.
		To move left set xcoord=-1.

		If you desire it to stop set both 0.

		Returns 'pop' message woth the last position or a crash message with [-1,-1]
		'''
		newpos = [self.head[0] + xcoord, self.head[1] + ycoord]
		
		## walk trough boundaries
		if newpos[0] < 0:
			newpos[0]=self.xlims
		if newpos[0] > self.xlims:
			newpos[0]=0
		if newpos[1] < 0:
			newpos[1]=self.ylims
		if newpos[1] > self.ylims:
			newpos[1]=0
		## crash on boundaries
		# if newpos[0]<0 or newpos[0]>self.get_xlims() or newpos[1]<0 or newpos[1]>self.get_ylims():
		# 	self.next_mov=[0,0]
		#	self.alive=False
		# 	return 'b_crash', [-1,-1]

		## check if crash it self
		if newpos in self.loc:
			self.next_mov=[0,0]
			self.alive=False
			return 's_crash',[-1,-1]

		self.loc.insert(0, newpos)
		self.next_mov=[xcoord, ycoord]
		if not growth:
			last_pos=self.loc.pop()
			msg='walk'
		else:
			last_pos=[-1,-1]
			msg='growth'
		
		self.update()
		return msg,last_pos


Snake.xlims=10
Snake.ylims=10
Snake.initial_size=3

def main():
	return

if __name__ == '__main__':
	main()
