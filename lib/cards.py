"""Main placeholder for Cards"""
import random
from enum import Enum
from typing import List, Tuple


class Suits(Enum):
    """Placeholder of card's suits"""

    HEART = "♥"
    DIAMOND = "♦"
    SPADE = "♠"
    CLUB = "♣"

    def __str__(self):
        return self.value


def get_suits() -> Tuple[str, ...]:
    return tuple([item.value for item in Suits])


def get_random_suit_index() -> Suits:
    def _get_shuffled_suits() -> list[Suits]:
        """
        The _get_shuffled_suits function returns a tuple of the suits in the deck, but shuffled.

        :return: A tuple of shuffled suits
        """
        shuffled_suits = list(Suits)
        random.shuffle(shuffled_suits)

        return shuffled_suits

    return random.choice(_get_shuffled_suits())


class Cards(object):
    """The Cards class is a placeholder for a card game."""

    def __init__(self):
        self.suited_cards = None
        self.refresh()

    def refresh(self) -> None:
        """The `refresh` method in the `Cards` class is used to reset
        the deck of cards. It initializes the `cards` list with the values of the cards
        (Ace to 10), and then creates a copy of this
        list for each suit in the `suits_cards` list. This ensures that each suit has its own set of
        cards.
        """
        ace = 11
        cards_list: List[int] = [ace] + list(range(2, ace))
        self.suited_cards = dict(
            zip(
                (Suits.HEART, Suits.DIAMOND, Suits.SPADE, Suits.CLUB),
                [cards_list.copy() for _ in range(len(cards_list))],
            )
        )

    def update_chosen_cards(func):
        def _remove_card(self):
            card = func(self)
            self.suited_cards[card[1]].remove(card[0])
            return card

        return _remove_card

    @update_chosen_cards
    def get_card(self) -> List[int | Suits]:
        """
        The function "get_card" returns a randomly selected card and
        its corresponding suit from a deck of
        cards.
        :return: A list containing a string representing a card (e.g. "Ace", "King", "Queen", etc.)
        and a string representing the suit of the card
        (e.g. "Hearts", "Diamonds", "Clubs", "Spades").
        """

        suit_index = get_random_suit_index()
        suited_cards = self.suited_cards[suit_index]
        card_index: int = random.choice(suited_cards)

        return [card_index, suit_index]


#  TESTS


if __name__ == "__main__":
    cards = Cards()
    for i in range(1, 6):
        test_card = cards.get_card()
        MESSAGE = (
            "Failed" if test_card[0] in cards.suited_cards[test_card[1]] else "Pass"
        )
        print(f"{i} - {test_card} isn't in cards - {MESSAGE}")
