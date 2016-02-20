'''
Shoe Class
-Simulates a shoe of cards in blackjack
-Can randomly generate a shoe of arbitrary number of decks
-By default, shoes are finished after 3/4 of the shoe
-Can pop one card at a time
-keeps track of the count internally
'''

import random

class Shoe:

	def __init__(self, num_decks):
		self.count = 0
		self.num_decks = num_decks
		self.generate_shoe()

	def is_finished(self):
		if self.pointer/52 > self.num_decks * 0.75:
			return True 
		return False

	def draw(self):
		card = self.cards[self.pointer]
		if card in [2,3,4,5,6]:
			self.count += 1
		elif card in [1, 10]:
			self.count -= 1

		self.pointer += 1
		return card

	def true_count(self):
		#adjust for human error
		decks_left = round(self.num_decks - self.pointer/52, 0)
		return self.count / decks_left

	def generate_shoe(self):
		self.pointer = 0
		self.cards = [0 for i in range(52 * self.num_decks)]
		indices = set(range(52 * self.num_decks))
		for i in range(1, 10):
			for j in range(self.num_decks * 4):
				index = random.sample(indices, 1)[0]
				indices.remove(index)
				self.cards[index] = i
		for i in range(4):
			for j in range(self.num_decks * 4):
				index = random.sample(indices, 1)[0]
				indices.remove(index)
				self.cards[index] = 10
