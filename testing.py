from cards import Card

def make_hand():
	hand = []

	for i in range(4):
		for j in range(4):
			hand.append(Card(Card.values[i], Card.suits[j]))
	return hand
