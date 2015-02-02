from random import shuffle

class Card:
	values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	suits = ['h', 's', 'd', 'c']

	def __init__(self, cardvalue, cardsuit):
		if not cardvalue.upper() in Card.values:
			raise InvalidValue('%r is an invalid card value.' % cardvalue)
		if not cardsuit.lower() in Card.suits:
			raise InvalidSuit('%r is an invalid card suit.' % cardsuit)

		self.val = cardvalue.upper()
		self.suit = cardsuit.lower()
		self.rank = Card.values.index(cardvalue.upper())
		self.suit_rank = Card.suits.index(self.suit)
		self.html_class = "card suit" + cardsuit.lower()
		self.html_img = "img/%s%s.png" % (self.suit, self.val.lower())

	def __repr__(self):
		return "%s of %s" % (self.val, self.suit)
		
class Hand:
	def __init__(self):
		self.cards = []

	def sort_hand(self):
		self.cards = sorted(self.cards, key=lambda x: (x.suit_rank, x.rank))				

	def num_cards(self):
		return len(self.cards)

class InvalidSuit(Exception):
	pass

class InvalidValue(Exception):
	pass
