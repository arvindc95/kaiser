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
		self.html_class = "card suit" + cardsuit.lower()

class InvalidSuit(Exception):
	pass

class InvalidValue(Exception):
	pass
