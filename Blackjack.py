# Shantanu Jain
# Blackjack client
# IAP 2015 1/21/2015

import random

suites = {'SPADES': 'SPADES', 'CLUBS': 'CLUBS', 'HEARTS': 'HEARTS', 'DIAMONDS': 'DIAMONDS'}
playerWins = 0

'''		
class Card:
"""Represents a card"""
	
	def __init__(self, suite, rank):
		self.suite = suite
		self.rank = rank
'''

class Deck:
	"""Represents a deck"""
	
	def __init__(self):
		self.cards = []
		for suite in suites:
			for rank in range(1, 14):
				self.cards.append((suite, rank))

	def shuffle(self):
		random.shuffle(self.cards)

	def draw(self):
		"""Draw card from top of deck, remove from deck"""
		return self.cards.pop(0)

class Player:
	"""Represents a player"""
	
	def __init__(self):
		self.hand = []
		self.wins = 0

	def getHandValue(self):
		value = 0
		for suite, rank in self.hand:
			if rank == 1:
				# Ace case
				value += 1
			elif rank <= 10:
				# Non Ace, non face card case
				value += rank
			elif 10 < rank < 14:
				value += 10
		return value

	def discardHand(self):
		self.hand = []

	def addToHand(self, card):
		self.hand.append(card)

	def didWin(self):
		self.wins += 1

	def __str__(self):
		return str(self.hand)

class Dealer(Player):
	"""Represents a dealer, plays by dealer rules"""
	def needCard(self):
		if self.getHandValue() < 17:
			return True
		return False

def playBlackJack():
	player = Player()
	dealer = Dealer()
	while True:
		playRound(player, dealer)

def playRound(player, dealer):
	# Get a new deck
	deck = Deck()
	deck.shuffle()

	# Discard old hands
	player.discardHand()
	dealer.discardHand()
	player.addToHand(deck.draw())

	while True:
		print('Player Hand ({}):'.format(player.getHandValue()) + str(player))
		action = str(raw_input('[H]it or [S]tay?'))[0].upper()
		if action == 'H':
			player.addToHand(deck.draw())
			if player.getHandValue() > 21:
				print("Player Bust!")
				break
			elif player.getHandValue() == 21:
				print("Blackjack!")
				break
		else:
			break

	while dealer.needCard():
		dealer.addToHand(deck.draw())
	print('Dealer Hand ({}):'.format(dealer.getHandValue()) + str(player))
	if dealer.getHandValue() > 21:
		print("Dealer Bust!")
	elif player.getHandValue() == 21:
		print("Blackjack!")

	# Find Winner
	# Both bust, or tie score
	if ((player.getHandValue() > 21 and dealer.getHandValue() > 21)
		or player.getHandValue() == dealer.getHandValue()):
		print("Draw")
	# Player bust, dealer good
	elif player.getHandValue() > 21 and dealer.getHandValue() <= 21:
		dealer.didWin()
		print("Dealer Wins!")
	# Dealer busts, player good
	elif dealer.getHandValue() > 21 and player.getHandValue() <= 21:
		player.didWin()
		print("Player Wins!")
	# No busts, player greater
	elif (player.getHandValue() > dealer.getHandValue() and player.getHandValue() <= 21):
		player.didWin()
		print("Player Wins!")
	# No busts, dealer greater
	elif player.getHandValue() < dealer.getHandValue() and dealer.getHandValue() <= 21:
		dealer.didWin()
		print("Dealer Wins!")

	print("Game Score: Player has {} wins, Dealer has {} wins".format(player.wins, dealer.wins))
	# elif player.getHandValue() <= 21 and dealer.getHandValue() <= 21:
	# 	if player.getHandValue() > dealer.getHandValue():
	# 		player.didWin()
	# 		print("Player Wins! Has {} wins".format(player.wins))
	# 	else:
	# 		dealer.didWin()
	# 		print("Dealer Wins! Has {} wins".format(dealer.wins))
	print('')

if __name__ == '__main__':
	playBlackJack()