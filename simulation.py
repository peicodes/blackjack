'''
In our simplified simulation, we assume there are other players
We don't care about their plays since it doesn't affect us
Therefore, we simply draw a set number of cards prior to each hand, then 1v1 the dealer

'''

from shoe import Shoe

class Simulation:

	MIN_BET = 15

	#go through the tables in this sequence

	#[a,b] where a is the dealer's face up card and b is the player's paired card
	PAIRED_TABLE = [
		['U' for i in range(11)], #dealer card == 0
		['U', 'P', 'H', 'H', 'H', 'H', 'H', 'H', 'P', 'S', 'S'], #1
		['U', 'P', 'P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S'], #2
		['U', 'P', 'P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S'], #3
		['U', 'P', 'P', 'P', 'H', 'D', 'P', 'P', 'P', 'P', 'S'], #4
		['U', 'P', 'P', 'P', 'P', 'D', 'P', 'P', 'P', 'P', 'S'], #5
		['U', 'P', 'P', 'P', 'P', 'D', 'P', 'P', 'P', 'P', 'S'], #6
		['U', 'P', 'P', 'P', 'H', 'D', 'H', 'P', 'P', 'S', 'S'], #7
		['U', 'P', 'H', 'H', 'H', 'D', 'H', 'H', 'P', 'P', 'S'], #8
		['U', 'P', 'H', 'H', 'H', 'D', 'H', 'H', 'P', 'P', 'S'], #9
		['U', 'P', 'H', 'H', 'H', 'H', 'H', 'H', 'P', 'S', 'S'], #10
	]

	#[a,b] where a is the dealer's face up card and b is the player's non-ace card
	#note: if hitting a card creates an equivalent situation, we need to consider that
	ACE_TABLE = [
		['U' for i in range(11)], #dealer card == 0
		['U', 'U', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'], #1
		['U', 'U', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'], #2
		['U', 'U', 'H', 'H', 'H', 'H', 'D', 'D', 'S', 'S', 'S'], #3
		['U', 'U', 'H', 'H', 'D', 'D', 'D', 'D', 'S', 'S', 'S'], #4
		['U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'S'], #5
		['U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'S'], #6
		['U', 'U', 'H', 'H', 'H', 'D', 'H', 'S', 'S', 'S', 'S'], #7
		['U', 'U', 'H', 'H', 'H', 'D', 'H', 'S', 'S', 'S', 'S'], #8
		['U', 'U', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'], #9
		['U', 'U', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'], #10
	]

	#[a,b] where a is the dealer's face up card and b is the player's hand value
	VALUE_TABLE = [
		['U' for i in range(21)], #dealer card == 0
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'], #1
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #2
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #3
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #4
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #5
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #6
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'], #7
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'], #8
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'], #9
		['U', 'U', 'U', 'U', 'U', 'H', 'H', 'H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S'], #10
	]



	def __init__(self, num_decks):
		self.shoe = Shoe(num_decks)
		self.balance = 0
		self.lower_balance = 0

	def run(self):
		while not self.shoe.is_finished():
			if self.shoe.true_count() > 0:
				self.balance += self.play()
				print("Balance: ", self.balance)

			#draw a number of cards for info
			for i in range(10):
				self.shoe.draw()

	def play(self): #play returns amount of money won/lost
		bet = self.MIN_BET
		dealer_hand = [self.shoe.draw(), self.shoe.draw()]
		player_hand = [self.shoe.draw(), self.shoe.draw()]

		#check for blackjacks first

		#run the player hand and stop if there's a loss
		player_result = self.run_player_hand(dealer_hand, player_hand)
		print("Player hand: ", player_hand)
		if player_result == 'P':
			
			
			print("Unimplemented Split")
			return 0
		elif player_result == 'DB':
			return -1 * bet * 2
		elif player_result == 'B':
			return -1 * bet

		#run the dealer hand if the player hasn't busted
		dealer_result = self.run_dealer_hand(dealer_hand)
		print("Dealer hand: ", dealer_hand)

		#get the bet value
		if player_result == 'DS':
			bet *= 2

		return self.hand_result(dealer_result, dealer_hand, player_result, player_hand) * bet

	def hand_result(self, dealer_result, dealer_hand, player_result, player_hand):
		#we'll need these more than once
		soft_value = self.soft_value(player_hand)
		dealer_soft_value = self.soft_value(dealer_hand)

		#finalize winner and return net gain/loss
		if dealer_result == 'B' or dealer_soft_value < soft_value: 
			return 1
		elif dealer_soft_value > soft_value:
			return -1
		else:
			return 0


	def run_player_hand(self, dealer_hand, player_hand):
		next_move = 'U'
		while True:
			#check if last move was double down
			if next_move == 'D':
				if self.hard_value(player_hand) > 21: return 'DB'
				return 'DS'

			#calc next move, including busts from a previous hit
			next_move = self.player_next_move(dealer_hand, player_hand)
			if next_move == 'H' or next_move == 'D':
				player_hand.append(self.shoe.draw())

			if next_move == 'S' or next_move == 'B' or next_move == 'P':
				return next_move

	def run_dealer_hand(self, dealer_hand):
		next_move = 'U'
		while True:
			if self.hard_value(dealer_hand) > 21: return 'B'
			if self.soft_value(dealer_hand) > 17: return 'S'
			dealer_hand.append(self.shoe.draw())

	def player_next_move(self, dealer_hand, player_hand):
		move = 'U'
		hard_value = self.hard_value(player_hand)
		if hard_value > 21: return 'B'
		if hard_value >= 17: return 'S' #unnecessary but improves performance

		if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
			return Simulation.PAIRED_TABLE[dealer_hand[0]][player_hand[0]]

		if 1 in player_hand and hard_value <= 11:
			return Simulation.ACE_TABLE[dealer_hand[0]][hard_value - 1]

		return Simulation.VALUE_TABLE[dealer_hand[0]][hard_value]

	def hard_value(self, hand):
		sum = 0
		for card in hand:
			sum += card
		return sum

	def soft_value(self, hand):
		ace = False
		sum = 0
		for card in hand:
			sum += card
			if card == 1:
				ace = True
		if sum <= 11:
			return sum + 10
		return sum
		