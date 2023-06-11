import random
cards:list[int] = [11]+[index for index in range(2,11)]
cards += [10]*4
cardsHearts:list[int] = cards.copy()
cardsDiamonds:list[int] = cards.copy()
cardsSpades:list[int] = cards.copy()
cardsClubs:list[int] = cards.copy()
suits:tuple[str] = ("Hearts","Diamonds","Spades","Clubs")
suitsCards:list[list[int]] = [cardsHearts,cardsDiamonds,cardsSpades,cardsClubs]

def getCard()->tuple[str,int]:
	suitIndex = random.randrange(0, len(suits))
	suitCards = suitsCards[suitIndex]
	card = suitCards.pop(random.randint(0, len(suitCards) - 1))

	return (suits[suitIndex],card)
