from random import randint
from time import sleep
from utilities.Clock import Clock
from threading import Thread

class Dice(object):
	def __init__(self):
		self.sides = 6
		self.side = 0
		self.clock = Clock()

	def roll(self):
		Thread(target = self.decide, args = (1, 6, 4)).start()
		while self.side == 0:
			pass
		side = self.side
		self.side = 0
		return side

	def decide(self, fmin, fmax, time):
		self.clock.start()
		starting = self.clock.get()
		started = starting
		while started <= (starting + time):
			for i in range(1, 6):
				face = randint(fmin, fmax)
			started += 1
		self.clock.stop()
		self.side = face

if __name__ == '__main__':
	dice = Dice()
	d1 = dice.roll()
	print(d1)
	input()