from random import randint
cards:list[int] = [index for index in range(2,12)]
cards += [10]*4
cardsHearts:list[int] = cards.copy()
cardsDiamonds:list[int] = cards.copy()
cardsSpades:list[int] = cards.copy()
cardsClubs:list[int] = cards.copy()
# 0-hearts, 1-diamonds, 2-spades, 3-clubs
suits:list[list[int]] = [cardsHearts,cardsDiamonds,cardsSpades,cardsClubs]

def getCard()->int:
	suit = suits[randint(0, len(suits) - 1)]
	card = suit.pop(randint(0, len(suit) -1))
	return card