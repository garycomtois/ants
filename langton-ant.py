# Langton's Ant
# green 
from tkinter import Tk, Canvas

class Ant(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('ant')
		self.my_width = 500
		self.my_height = 500
		self.ylen = 4
		self.xlen = 4
		self.d = 4
		self.c = Canvas(self, width=self.my_width,\
		height=self.my_height)
		self.c.pack()
		self.x = 300
		self.y = 300
		self.facing = 'west'
		# 0 = white, 1 = green. Init tiles array to all white.
		self.tiles = [0]*self.my_width*self.my_height
		
	def get_colormove(self):
		''' Called first. Calc index of tile array based on y (row) and
		x (column). '''
		yndx = self.y*self.my_height
		ndx = int(yndx + self.x)
		if self.tiles[ndx] == 0:
			self.next_color = 'green'
			self.move = 'right'
		else:
			self.next_color = 'white'
			self.move = 'left'
	
	def draw(self):
		''' Called second. Color pixel at our position. '''
		self.c.create_rectangle(self.x,\
		self.y+self.ylen,\
		self.x+self.xlen,\
		self.y,\
		fill=self.next_color,outline="")	
	
	def store_color(self):
		''' Called third. Writes current tile color to tiles list. '''
		yndx = self.y*self.my_height
		ndx = int(yndx + self.x)
		if self.next_color.startswith('green'):
			self.tiles[ndx] = 1
		else:
			self.tiles[ndx] = 0
		
	def set_deltas(self):
		''' Called forth. Incr/decrements x or y, sets ant's position. ''' 
		# white = right, green = left
		if self.facing.startswith('north'):
			if self.move.startswith('right'):
				self.facing = 'east'
				self.x += self.d
			else:
				self.facing = 'west'
				self.x -= self.d
		elif self.facing.startswith('east'):
			if self.move.startswith('right'):
				self.facing = 'south'
				self.y += self.d
			else:
				self.facing = 'north'
				self.y -= self.d
		elif self.facing.startswith('south'):
			if self.move.startswith('right'):
				self.facing = 'west'
				self.x -= self.d
			else:
				self.facing = 'east'
				self.x += self.d
		elif self.facing.startswith('west'):
			if self.move.startswith('right'):
				self.facing = 'north'
				self.y -= self.d
			else:
				self.facing = 'south'
				self.y += self.d
			
	def next_frame(self):
		# 1. Get color of our position (and next move).
		self.get_colormove()
		# 2. Color box.
		self.draw()
		# 3. Store this color to the tiles list.
		self.store_color()		
		# 4. Calc next x,y coords.
		self.set_deltas()
		self.c.after(1, self.next_frame)

if __name__ == "__main__":
	app = Ant()
	app.next_frame()
	app.mainloop()
