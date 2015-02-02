from cards import Card, Hand
from random import randint

def test_hand():
	hand = Hand()
	for i in range(2):
		for j in range(4):
			hand.cards.append(Card(Card.values[randint(0,12)], Card.suits[randint(0, 3)]))
	hand.sort_hand()
	return hand
