# Langton's Ant
# green 
from tkinter import Tk, Canvas

class Ant(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('ant')
		self.my_width = 800
		self.my_height = 800
		self.ylen = 5
		self.xlen = 5
		self.d = 5
		self.c = Canvas(self, width=self.my_width,\
		height=self.my_height)
		self.c.pack()
		self.x = self.my_width/2
		self.y = self.my_height/2
		self.facing = 'north'
		# 0 = white, 1 = green
		self.tiles = [0]*self.my_width*self.my_height
		
	def get_colormove(self):
		yndx = self.y*self.my_height
		ndx = int(yndx + self.x)
		if self.tiles[ndx] == 0:
			self.next_color = 'green'
			self.move = 'right'
		else:
			self.next_color = 'white'
			self.move = 'left'
		
	def store_color(self):
		yndx = self.y*self.my_height
		ndx = int(yndx + self.x)
		if self.next_color.startswith('green'):
			self.tiles[ndx] = 1
		else:
			self.tiles[ndx] = 0
		
	def set_deltas(self):
		# white = right, green = left
		if self.facing == 'north':
			if self.move == 'right':
				self.facing = 'east'
				self.x += self.d
				# no change to y
			else:
				self.facing = 'west'
				self.x -= self.d
				# no change to y
		elif self.facing == 'east':
			if self.move == 'right':
				self.facing = 'south'
				self.y += self.d
			else:
				self.facing = 'north'
				self.y -= self.d
		elif self.facing == 'south':
			if self.move == 'right':
				self.facing = 'west'
				self.x -= self.d
			else:
				self.facing = 'east'
				self.x += self.d
		elif self.facing == 'west':
			if self.move == 'right':
				self.facing = 'north'
				self.y -= self.d
			else:
				self.facing = 'south'
				self.y += self.d
			
	def next_frame(self):
		# get color of our position (and next move)
		self.get_colormove()
		# color pixel at our position
		self.c.create_rectangle(self.x,\
		self.y+self.ylen,\
		self.x+self.xlen,\
		self.y,\
		fill=self.next_color,outline="")
		#print('x=%i, y=%i, %s, %s' % (self.x,self.y,self.next_color,self.facing))
		self.store_color()		
		# set next x,y coords
		self.set_deltas()
		#print('\t\t\t%s' % self.facing)
		self.c.after(25, self.next_frame)

if __name__ == "__main__":
	app = Ant()
	app.next_frame()
	app.mainloop()