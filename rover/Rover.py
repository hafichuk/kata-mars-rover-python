from rover.Directions import North

class Rover:
	def __init__(self, position=None, orientation=North):
		if position is None:
			position = {'x':0,'y':0}

		self.position = position
		self.orientation = orientation
		self.commands = {'f': self.forward, 'b': self.backward, 'r': self.right, 'l': self.left}

	def getPosition(self):
		return self.position

	def getOrientation(self):
		return self.orientation

	def left(self):
		self.orientation = self.orientation.left()
		return self.orientation

	def right(self):
		self.orientation = self.orientation.right()
		return self.orientation

	def forward(self):
		self.position['x'] += self.orientation.x
		self.position['y'] += self.orientation.y
		return self.position

	def backward(self):
		self.position['x'] -= self.orientation.x
		self.position['y'] -= self.orientation.y
		return self.position

	def move(self, commands):
		for command in commands:
			if command in self.commands.keys():
				self.commands[command]()
			else:
				raise ValueError("Invalid command [%s] in sequence: [%s]" % (command, commands)) 

	def getStatus(self):
		return {'x': self.position['x'], 'y': self.position['y'], 'd': self.orientation.name}