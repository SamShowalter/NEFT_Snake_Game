

class Snake():

	def __init__(self, seg_size, direction = "Left"):
		self.direction = direction
		self.seg_size = seg_size
		self.body = []

	def addSegment(self, segment):
		self.body.append(segment) 


	def move_helper(self,move_x,move_y):
		
		for seg_index in reversed(range(1, len(self.body))):
			self.body[seg_index].updateLocation(self.body[seg_index-1])

		self.body[0].shiftLocation(move_x*(self.seg_size),move_y*(self.seg_size))

		#Print statement for debugging
		#print(self.body[0].x,self.body[0].y)

		

	def change_direction(self, direction):
		self.direction = direction

	def move(self):
		if (self.direction == "Up"):
			self.move_helper(0,-1)
		elif (self.direction == "Down"):
			self.move_helper(0,1)
		elif (self.direction == "Left"):
			self.move_helper(-1,0)
		elif (self.direction == "Right"):
			self.move_helper(1,0)





