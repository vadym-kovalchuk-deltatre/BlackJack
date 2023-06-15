import random

cards: list[int] = [11] + [card_range for card_range in range(2, 11)]  # starts from Ace = 11
cards += [10] * 4
cards_Hearts: list[int] = cards.copy()
cards_Diamonds: list[int] = cards.copy()
cards_Spades: list[int] = cards.copy()
cards_Clubs: list[int] = cards.copy()
suits: tuple[str, str, str, str] = ("♥", "♦", "♠", "♣")
suits_cards: list[list[int]] = [cards_Hearts, cards_Diamonds, cards_Spades, cards_Clubs]


def get_card() -> list[str, int]:
    """
    The function "get_card" returns a randomly selected card and
    its corresponding suit from a deck of
    cards.
    :return: A list containing a string representing a card (e.g. "Ace", "King", "Queen", etc.) and a
    string representing the suit of the card (e.g. "Hearts", "Diamonds", "Clubs", "Spades").
    """
    suit_index = random.randrange(0, len(suits))
    suit_cards = suits_cards[suit_index]
    card = suit_cards.pop(random.randint(0, len(suit_cards) - 1))

    return [card, suits[suit_index]]
